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

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, related_name="news", verbose_name="Автор", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, verbose_name="Статус", choices=NewsStatus.choices, default=NewsStatus.CREATED)
    date_created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    author = models.ForeignKey(User, related_name="comments", verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    new = models.ForeignKey(New, related_name="comments", verbose_name="Новость", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания")

    def __str__(self):
        # return "Комментарий "+self.author.username
        return self.text
