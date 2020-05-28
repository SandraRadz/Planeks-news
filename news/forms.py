from django import forms
from django_summernote.widgets import SummernoteWidget

from news.models import New


class CommentForm(forms.Form):
    text = forms.CharField(label="Комментарий")

    def send_email(self):
        print("send email")


class NewForm(forms.Form):
    title = forms.CharField(label="Заголовок")
    text = forms.CharField(label="Текст", widget=SummernoteWidget())
