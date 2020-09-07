# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework import viewsets, generics

from .models import Movie
from .serializers import MovieSerializer


class MovieListView(ListView):
    """Show all movies."""

    model = Movie

    def get_queryset(self):
        return Movie.objects \
            .annotate(avg_rating=Avg('ratings__stars')) \
            .order_by('-released_on', '-avg_rating')


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie
    pk_url_kwarg = "id"


class MovieCreateView(SuccessMessageMixin, CreateView):
    """Create a new movie."""

    model = Movie
    fields = ['title', 'year', 'rated', 'released_on', 'genre', \
        'director', 'plot']
    success_message = "The movie created successfully"

    def form_invalid(self, form):
        messages.error(self.request, 'The creation has failed')
        return self.render_to_response(self.get_context_data(request=self.request, form=form))


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested movie."""

    model = Movie
    pk_url_kwarg = "id"
    fields = ['title', 'year', 'rated', 'released_on', 'genre', \
        'director', 'plot']
    success_message = "The movie updated successfully"

    def form_invalid(self, form):
        messages.error(self.request, 'The update has failed')
        return self.render_to_response(self.get_context_data(request=self.request, form=form))


class MovieDeleteView(SuccessMessageMixin, DeleteView):
    """Delete the requested movie."""

    model = Movie
    pk_url_kwarg = "id"

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'The movie deleted successfully')
        return reverse_lazy('movies:index')


class MovieViewSetAPI(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.order_by('-released_on')

class MovieRetrieveAPI(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
