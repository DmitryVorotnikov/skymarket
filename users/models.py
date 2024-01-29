from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    class RoleType(models.TextChoices):
        # CHOICES для роли пользователей.
        USER = 'USER', 'Обычный пользователь'
        MANAGER = 'MANAGER', 'Менеджер/персонал'
        # ADMIN - is_staff=True, 'Админ'

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = PhoneNumberField(verbose_name='Телефонный номер')
    image = models.ImageField(upload_to='users/', verbose_name='Фото пользователя', **NULLABLE)
    role = models.CharField(max_length=25, choices=RoleType.choices, default=RoleType.USER, verbose_name='Роль', **NULLABLE)
    token = models.CharField(max_length=200, verbose_name='Токен для смены пароля', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}, {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)
