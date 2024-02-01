from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    fio = models.CharField(max_length=150, verbose_name='ФИО', **NULLABLE)
    about = models.TextField(verbose_name='коментарии', **NULLABLE)
    token = models.CharField(max_length=22, verbose_name='Token для верификации почты', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='верифицированна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('email',)
