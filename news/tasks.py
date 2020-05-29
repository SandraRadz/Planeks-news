from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.conf import settings
from django.template import loader

from myuser.mail_sender import MailSender


@shared_task
def send_comment_letter(comment_id):
    from news.models import Comment
    comment = Comment.objects.get(pk=comment_id)
    html_message = loader.render_to_string(
        'news/letter.html',
        {
            'user': comment.author,
            'new': comment.new.title,
        }
    )
    MailSender.send_html("Новый комментарий", html_message, settings.LETTER_FROM, comment.new.author.email)
