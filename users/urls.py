# coding=utf-8
from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^register$',views.createUser,name='users_register'),
    url(r'^login$',views.login,name='users_login'),

]