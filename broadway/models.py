from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Movie(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField()
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


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

    name = models.CharField(max_length=30)
    number = models.CharField(max_length=100)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='cinema')


class Seat(models.Model):

    number_seat = models.CharField(max_length=70)
    row_number = models.PositiveIntegerField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="seat")


class Feedback(models.Model):#обратная связь
    rate_choices = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
    ]
    rate = models.IntegerField(choices=rate_choices)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    comment = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)


class ShowTime(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="showtime")
    start_time = models.DateTimeField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    total_sum = models.PositiveIntegerField(default=0, null=True)



class Ticket(models.Model):
    price = models.IntegerField()
    seats = models.OneToOneField(Seat,on_delete=models.SET_NULL, null=True, related_name='ticket')
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='showtime')
    start_time = models.DateTimeField()
    payment_methods = (
        ('card', 'card'),
        ('cash', 'cash'),
    )


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
