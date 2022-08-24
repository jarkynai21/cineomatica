from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, views, status
from .models import *
from .serializers import UserSerializer, HistorySerializer, FeedbackSerializer, TicketSerializer, ShowTimeSerializer, \
    MovieSerializer, SeatSerializer, RoomSerializer, CinemaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class CinemaView(views.APIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request,*args,**kwargs):
        cinema = Cinema.objects.all()
        serializer = CinemaSerializer(cinema,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def delete(self, request,*args,**kwargs):
        count = Cinema.objects.all().delete()
        return Response({'{} Cinema were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)



class UserView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def delete(self, request,*args,**kwargs):
        count = User.objects.all().delete()
        return Response({'{} User were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)


class MovieView(views.APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAdminOrReadOnly, )

    def get(self,request,*args,**kwargs):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def delete(self, request,*args,**kwargs):
        count = Movie.objects.all().delete()
        return Response({'{} Movie were deleted successfully!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer



class ShowTimeViewSet(viewsets.ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer



class TicketView(views.APIView):

    def get(self,request,*args,**kwargs):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket,many=True)
        return Response(serializer.data)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer