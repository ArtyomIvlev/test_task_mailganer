# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import CustomUser
from django.contrib import admin


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('username',
                    'email',
                    'date_joined',
                    )
