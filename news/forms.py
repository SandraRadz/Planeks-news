from django import forms


class CommentForm(forms.Form):
    text = forms.CharField()

    def send_email(self):
        print("send email")
