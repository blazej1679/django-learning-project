# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


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
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Dodanie nowego wpisu przynależącego do tematu."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano zadych danych, tworzenie pustego formularza.
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edycja stniejacego wpisu."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=Entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
