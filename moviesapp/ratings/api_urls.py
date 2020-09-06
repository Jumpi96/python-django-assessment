# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.RatingCreateListAPI.as_view(), name="")
]
