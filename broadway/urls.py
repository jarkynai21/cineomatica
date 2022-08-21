from .views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()

urlpatterns = [

    path('user/',UserView.as_view()),
    path('cinema/', CinemaView.as_view()),
    path('movie/', MovieView.as_view()),
    path('ticket/', TicketView.as_view()),

]