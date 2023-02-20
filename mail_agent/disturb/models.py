# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Disturb(models.Model):
    """Модель рассылки."""
    pass


class Follower(models.Model):
    """Модель подписчкиков для рассылки."""
    name = models.CharField(
        verbose_name='Имя подписчика',
        max_length=20,
    )
    surname = models.CharField(
        verbose_name='Фамилия подписчика',
        max_length=20,
    )
    b_day = models.DateField(
        verbose_name='Дата рождения'
    )
    email = models.EmailField(
        verbose_name='Почта подписчика',
    )


class Message(models.Model):
    """Модель макета письма."""
    maket = models.TextField(
        verbose_name='Макет письма.'
    )
