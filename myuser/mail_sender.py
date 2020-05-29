from django.core.mail import send_mail


class MailSender:

    @staticmethod
    def send_plain_text(title, message, email_from, email_to):
        send_mail(title, message, email_from, [email_to],
                  fail_silently=False)

    @staticmethod
    def send_html(title, message, email_from, email_to):
        send_mail(title, message, email_from, [email_to],
                  fail_silently=False, html_message=message)