# coding=utf-8
from django.conf.urls import *
from . import views

urlpatterns = [
    #url(r'^register$',views.createUser,name='users_register'),
    url(r'^$',views.showindex,name='show_index'),
    url(r'^update_news$',views.news_update,name='update_news'),
    url(r'^getnews$',views.get_news,name='get_news'),
]