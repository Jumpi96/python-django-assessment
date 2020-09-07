from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'rated', 'released_on', 'genre', \
            'director', 'plot', 'avg_ratings', 'num_ratings', 'id']