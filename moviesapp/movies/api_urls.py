# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'', views.MovieViewSetAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>', views.MovieRetrieveAPI.as_view(), name="get_movie")
]
