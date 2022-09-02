from rest_framework import serializers
from .models import *
import datetime


class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'title', 'image', 'address', 'contact', 'schedule']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def movie(obj):
        now = datetime.date.today()
        if obj.start_date <= now <= obj.end_date:
            obj.movie = "current" #текущий
            return obj.movie
        if obj.start_date > now:
            obj.movie = "upcoming" #предстоящий
            return obj.movie


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

    def create(self, validated_data):
        seat = validated_data.pop
        row = validated_data.pop
        for row in range(1, seat + 1):
            for seat in range(1, row + 1):
                seats = Seat.obj.create(seat=seat, row=row **validated_data)
        return seats




class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = ["id", "movie", "creation_date", "room"]


class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()

    class Meta:
         model = Order
         fields = "__all__"


    def get_total_price(self, obj):
        total_price = 0
        try:
            total_price += obj.quantity * obj.ticket.price
            obj.total_sum = total_price
            obj.save()
            obj.user.wallet -= total_price
            obj.user.save()
            return total_price
        except AttributeError:
            return 0


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

