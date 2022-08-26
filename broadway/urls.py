from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()

urlpatterns = [

    path('user/',UserViewSet.as_view()),
    path('cinema/', CinemaViewSet.as_view()),
    path('movie/', MovieViewSet.as_view()),
    path('ticket/', TicketViewSet.as_view()),

]