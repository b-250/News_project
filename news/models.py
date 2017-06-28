# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
import getnews
# Create your models here.
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "newsbackend.settings"})

channel_list = ['头条', '新闻', '财经', '体育', '娱乐', '军事', '教育', '科技', 'NBA', '股票']

class Mynews(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    title = models.CharField(max_length=100, unique=True)
    channel = models.CharField(max_length=10)
    weburl = models.CharField(max_length=200)
    mobileurl = models.CharField(max_length=200)
    pic = models.CharField(max_length=60)
    time = models.CharField(max_length=20)
    src = models.CharField(max_length=10)
    savepath = models.CharField(max_length=100)