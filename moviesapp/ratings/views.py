
from django.views.generic import CreateView
from rest_framework import generics

from .models import Rating
from .serializers import RatingSerializer


class RatingCreateView(CreateView):
    """Create a new rating for a movie."""

    model = Rating
    fields = ['stars', 'comment', 'movie']


class RatingCreateListAPI(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
