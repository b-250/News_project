# coding=utf-8
from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^register$',views.createUser,name='users_register'),
    url(r'^login$',views.Mylogin,name='users_login'),
    url(r'^logout$',views.Mylogout,name='users_logout'),
    url(r'^islogin$', views.islogin,name='is_user_is_login'),
]