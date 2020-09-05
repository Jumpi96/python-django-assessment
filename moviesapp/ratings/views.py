
from django.views.generic import CreateView
from .models import Rating


class RatingCreateView(CreateView):
    """Create a new rating for a movie."""

    model = Rating
    fields = ['stars', 'comment', 'movie']
