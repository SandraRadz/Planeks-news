from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string

from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic

from myuser.forms import UserCreationForm, UserLogInForm
from myuser.mail_sender import MailSender
from django.conf import settings

from myuser.models import MyUser
from news.token_creator import TokenGenerator


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

    @staticmethod
    def __create_token(user):
        pass

    def form_valid(self, form):
        user = form.save()
        generator = TokenGenerator()
        email = form.cleaned_data['email']
        message = render_to_string('myuser/activate_letter.html', {
            'user': user,
            'domain': settings.APP_DOMAIN,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generator.make_token(user),
        })
        MailSender.send_html("Подтвердите email", message, settings.LETTER_FROM, email)
        auth = authenticate(self.request, email=email, password=form.cleaned_data['password1'])
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


def activate_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, MyUser.DoesNotExist):
        user = None
    if user is not None and TokenGenerator.check_token(user, token):
        user.is_approved = True
        user.save()
        return redirect(reverse('news-list'))
    else:
        return HttpResponse('Activation link is invalid!')
