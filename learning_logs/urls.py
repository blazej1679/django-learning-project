"""Definiowanie wzorcow adresow URL dla aplikacji learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #strona glowna
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    #wyswietlenie wszystkich tematow
    #url(r'^topics/$', views.topics, name='topics'),
    path('topics/', views.topics, name='topics'),

    #url(r"^topics/(?P<topic_id>\d+)/$", views.topic, name='topic'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    path('new_topic/', views.new_topic, name='new_topic'),
    #url(r'^new_topic/$', views.new_topic, name='new_topic'),

    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]