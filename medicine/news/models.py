from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class NewsArticle(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    published_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        "Изображение",
        upload_to='news/media/',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:news_article_detail", kwargs={"pk": self.pk})
