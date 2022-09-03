from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Movie(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    start_date = models.DateField()
    end_date = models.DateField()


class Cinema(models.Model):

    name = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    image = models.ImageField()
    schedule = models.CharField(max_length=100, verbose_name='расписание')
    contact = models.CharField(max_length=100, verbose_name='контакты')
    address = models.CharField(max_length=100, verbose_name='адрес')

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Room(models.Model):

    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='cinema')
    name = models.CharField(max_length=55, default=None)


class Seat(models.Model):

    seat = models.CharField(max_length=70)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="seat")
    row = models.PositiveIntegerField(blank=True,null=True)


class Feedback(models.Model):#обратная связь

    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    comment = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)


class ShowTime(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='showtime')
    creation_date = models.DateTimeField(default=timezone.now)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total_sum = models.PositiveIntegerField(default=0, null=True)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(default=0, null=True)


class Ticket(models.Model):
    price = models.PositiveIntegerField(default=0)
    seat = models.OneToOneField(Seat,on_delete=models.SET_NULL, null=True, related_name='ticket')
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='showtime')
    start_time = models.DateTimeField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name="order")
    booking = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="booking")
    payment_methods = (
        ('card', 'card'),
        ('cash', 'cash'),
    )



class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    discount = models.FloatField(default=0)