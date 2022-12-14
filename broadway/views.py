from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, views, status
from .models import *
from .serializers import UserSerializer, FeedbackSerializer, TicketSerializer, ShowTimeSerializer, \
    MovieSerializer, SeatSerializer, RoomSerializer, CinemaSerializer, OrderSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


class CinemaView(views.APIView):

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request,*args,**kwargs):
        cinema = Cinema.objects.all()
        serializer = CinemaSerializer(cinema,many=True)
        return Response(serializer.data)


class UserView(views.APIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get(self,request,*args,**kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class MovieView(views.APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request,*args,**kwargs):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie,many=True)
        return Response(serializer.data)


class RoomView(views.APIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class SeatView(views.APIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def get(self,request,*args,**kwargs):
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats,many=True)
        return Response(serializer.data)



class ShowTimeView(views.APIView):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer

    def get(self,request,*args,**kwargs):
        showtime = ShowTime.objects.all()
        serializer = ShowTimeSerializer(showtime,many=True)
        return Response(serializer.data)


class TicketView(views.APIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get(self, request):
        ticket = Ticket.objects.all()
        if ticket is not None:
            ticket = Ticket.filter()

        ticket_serializer = TicketSerializer(ticket, many=True)
        return Response(ticket_serializer.data)

    def post(self, request):
        user = Ticket.objects.get(seat=["seat"], show_time=["show_time"]).user
        if request.user == user:
            Ticket.objects.get_create(seat=["seat"], show_time=["show_time"])
        elif Ticket.objects.filter(seat=["seat"], show_time=["show_time"]):
            Ticket.objects.create(seat=["seat"], show_time=["show_time"])
        else:
            return Response('Ticket booked!')


    def create(self, attrs, *validated_data):
        user = self.context["request"].user
        attrs.booking = user
        if validated_data.get("payment_method"):
            attrs.payment_method = validated_data.get("payment_method", attrs.payment_method)
            order = Order.objects.create(total_price=attrs.price, user=user)
            attrs.order = order
        attrs.save()
        return attrs


class FeedbackView(views.APIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self,request,*args,**kwargs):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback,many=True)
        return Response(serializer.data)


class OrderView(views.APIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self,request,*args,**kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CartView(views.APIView):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self,request,*args,**kwargs):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart,many=True)
        return Response(serializer.data)