# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms

# posts/views.py
from django.views.generic import ListView
from .models import Post

from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy, reverse # new

class HomePageView(ListView):
    model = Post
    template_name = 'image_processor/home.html'

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover']

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'image_processor/post.html'
    success_url = reverse_lazy('image_processor:home')