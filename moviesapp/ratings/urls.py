# -*- coding: utf-8 -*-
from django.urls import path

from . import views


urlpatterns = [
    path('create', view=views.RatingCreateView.as_view(), name='create'),
]
