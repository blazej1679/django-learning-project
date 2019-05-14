"""Definiowanie wzorcow adresow URL dla aplikacji learning_logs."""

from django.conf.urls import include, url

from . import views

urlpatterns = [
    #strona glowna
    url(r'^$', views.index, name='index'),
    #wyswietlenie wszystkich tematow
    url(r'^topics/$', views.topics, name='topics'),
    url(r"^topics/(?P<topic_id>\d+)/$", views.topic, name='topic'),
]