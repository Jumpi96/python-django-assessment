# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from moviesapp.ratings.models import Rating
from statistics import mean


class Movie(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    year = models.PositiveIntegerField(default=2019)
    rated = models.CharField(max_length=64) # Example: PG-13
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def rating(self):
        ratings = [r.stars for r in Rating.objects.filter(movie=self)]
        return (mean(ratings), len(ratings)) if ratings else (0, 0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', args=[self.pk])
