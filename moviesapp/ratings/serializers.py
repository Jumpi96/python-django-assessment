
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from moviesapp.movies.models import Movie
from .models import Rating

class RatingSerializer(HyperlinkedModelSerializer):
    movie = PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Rating
        fields = ['stars', 'movie', 'comment']
