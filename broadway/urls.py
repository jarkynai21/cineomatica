from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r"user", UserView, basename='user')
router.register(r"cinema", CinemaView, basename="cinema")
router.register(r"movie", MovieView, basename="movie")



urlpatterns = [

    path("", include(router.urls)),


]