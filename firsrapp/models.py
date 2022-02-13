from django.db import models

# Create your models here.
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=' ')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='findnews')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return "/views_news/%i" % self.pk

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_date']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория новости')

    def get_absolute_url(self):
        return "/category/%i" % self.pk

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
