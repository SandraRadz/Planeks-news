from django import forms
from django_summernote.widgets import SummernoteWidget

from news.models import New


class CommentForm(forms.Form):
    text = forms.CharField()

    def send_email(self):
        print("send email")


class NewForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=SummernoteWidget())

# class NewForm(forms.ModelForm):
#     class Meta:
#         model = New
#         fields = ['text']
#         widgets = {
#             'text': SummernoteWidget(),
# }