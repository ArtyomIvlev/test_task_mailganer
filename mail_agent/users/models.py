# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CustomUser(AbstractUser):
    """Переопределённая модель пользователя."""
    email = models.EmailField(
        verbose_name='User Email',
        unique=True,
        max_length=254,
    )


@python_2_unicode_compatible
class CustomUserfollow(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='owners'
    )
    follower = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='followers',
    )

