from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect

from django.urls import reverse
from django.views import generic

from myuser.forms import UserCreationForm, UserLogInForm


class LogInView(generic.FormView):
    template_name = "myuser/log_in.html"
    form_class = UserLogInForm

    def form_valid(self, form):
        user = authenticate(self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Логин или пароль не верный")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('news-list')


class SignUpView(generic.FormView):
    form_class = UserCreationForm
    template_name = "myuser/sign_up.html"

    def form_valid(self, form):
        form.save()
        auth = authenticate(self.request, email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        if auth:
            login(self.request, auth)
            return super().form_valid(form)
        else:
            form.add_error(None, "Логин или пароль не верный")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('news-list')


def logout_view(request):
    logout(request)
    return redirect(reverse('news-list'))
