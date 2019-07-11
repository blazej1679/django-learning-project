"""Definiowanie wzorcow adresow URL dla aplikacji learning_logs."""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #Main site.
    #url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),

    #Site showing every topic.
    #url(r'^topics/$', views.topics, name='topics'),
    path('topics/', views.topics, name='topics'),

    #Site showing specific topic and corelated entries.
    #url(r"^topics/(?P<topic_id>\d+)/$", views.topic, name='topic'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Site to add new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    #url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #Site to add new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    #Site to edit one entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]