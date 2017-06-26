# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    nikename = models.CharField(
        max_length=32,
        verbose_name='昵称'
    )
    phone = models.CharField(
        max_length=11,
        verbose_name='手机'
    )