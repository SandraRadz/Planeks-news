import logging

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from myuser.mail_sender import MailSender
from news.token_creator import TokenGenerator


@shared_task
def send_confirmation_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        generator = TokenGenerator()
        email = user.email
        message = render_to_string('myuser/activate_letter.html', {
            'user': user,
            'domain': settings.APP_DOMAIN,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generator.make_token(user),
        })
        MailSender.send_html("Подтвердите email", message, settings.LETTER_FROM, email)
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)

