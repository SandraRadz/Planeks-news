from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.Form):
    text = forms.CharField(label="Комментарий")


class NewForm(forms.Form):
    title = forms.CharField(label="Заголовок")
    text = forms.CharField(label="Текст", widget=SummernoteWidget())
