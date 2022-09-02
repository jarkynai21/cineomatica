from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register(r"user", UserModelViewSet, basename='user')
router.register(r"cinema", CinemaModelViewSet, basename="cinema")
router.register(r"movie", MovieModelViewSet, basename="movie")



urlpatterns = [

    path("", include(router.urls)),


]