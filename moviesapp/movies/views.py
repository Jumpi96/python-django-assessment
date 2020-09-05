# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""

    model = Movie
    ordering = ['-released_on']


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie


class MovieCreateView(CreateView):
    """Create a new movie."""

    model = Movie
    fields = ['title', 'year', 'rated', 'released_on', 'genre', \
        'director', 'plot']


class MovieUpdateView(UpdateView):
    """Update the requested movie."""


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""

    model = Movie

    def get_success_url(self):
        return reverse_lazy('movies:index')
