from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    description = models.TextField(max_length=1000, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='ads/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)
