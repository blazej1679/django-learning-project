# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm
from .models import Topic

def index(request):
    """Strona glowna aplikacji learning_log."""

    return render(request, 'learning_logs/index.html')

def topics(request):
    """Wyswietla wszystkie tematy."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Wyswietla pojedynczy temat i wszytkie wpisy powiazane z nim."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Dodawanie nowego tematu."""
    if request.method != 'POST':
        #Nie przekazano zadnych danych, nalezy utworzyc pusty formularz.
        form = TopicForm()
    else:
        #Przekazano dane za pomocą zadania POST
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)