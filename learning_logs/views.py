# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    """Strona glowna aplikacji learning_log."""

    return render(request, 'learning_logs/index.html')