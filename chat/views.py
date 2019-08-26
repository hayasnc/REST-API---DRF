# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})