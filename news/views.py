from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from news.forms import CommentForm, NewForm
from news.models import New, Comment


class NewsList(generic.ListView):
    queryset = New.objects.filter(status='A').order_by('-pub_date')
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewDisplay(generic.DetailView):
    queryset = New.objects.filter(status='A')
    template_name = 'news/new_item.html'
    context_object_name = 'new_item'

    def get_context_data(self, **kwargs):
        context = super(NewDisplay, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


# todo login_required
class NewComment(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.FormView):
    template_name = 'news/new_item.html'
    form_class = CommentForm
    model = New

    def form_valid(self, form):
        Comment.objects.create(author=self.request.user, text=form.cleaned_data['text'], new=self.get_object())
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('new-item', kwargs={'pk': self.kwargs['pk']})


class NewDetail(generic.View):
    def get(self, request, *args, **kwargs):
        view = NewDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = NewComment.as_view()
        return view(request, *args, **kwargs)


# todo login_required
class CreateNew(LoginRequiredMixin, generic.FormView):
    template_name = "news/add_new.html"
    form_class = NewForm

    def form_valid(self, form):
        New.objects.create(author=self.request.user, text=form.cleaned_data['text'], title=form.cleaned_data['title'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # todo "thanks for your suggestion"|new-item/pk
        return reverse('news-list')
