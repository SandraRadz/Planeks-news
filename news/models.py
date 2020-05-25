from django.contrib.auth.models import User
from django.db import models


class New(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    class NewsStatus(models.TextChoices):
        CREATED = 'C', 'создано'
        APPROVE = 'A', 'одобрено'
        DECLINE = 'D', 'отклонено'

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, related_name="news", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=NewsStatus.choices, default=NewsStatus.CREATED)
    date_created = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    new = models.ForeignKey(New, related_name="comments", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Комментарий "+self.author.username
