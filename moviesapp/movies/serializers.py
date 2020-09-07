from rest_framework import serializers
from .models import Movie
from moviesapp.ratings.serializers import RatingSerializer

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'year', 'rated', 'released_on', 'genre', \
            'director', 'plot', 'avg_ratings', 'num_ratings', 'id', 'ratings']
