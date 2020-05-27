from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class New(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        permissions = [('can_publish_new_without_approve', 'Публикация новостей без премодерации')]

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

    def save(self, *args, **kwargs):
        """
            * create
                if user has permission can_publish_new_without_approve,
                new will be approved and pub_date will be set on now immediately
            * edit
                after someone has edited new,
                check whether value of status is equal to "approved" and
                if this new hasn't been approved before set pub_date value on now
        """
        if self.pk is None and self.author.has_perm('news.can_publish_new_without_approve'):
            self.status = "A"
            self.pub_date = datetime.now()
        if self.status == 'A' and self.pub_date is None:
            self.pub_date = datetime.now()
        return super().save(*args, **kwargs)

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
        return "Комментарий "+self.author.username
