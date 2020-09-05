
from django.urls import reverse
from django.db import models


class Rating(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    comment = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def get_absolute_url(self):
        return reverse('movies:detail', args=[self.movie.pk])