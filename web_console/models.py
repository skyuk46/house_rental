from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(default='',max_length=50, unique=True)
    email = models.EmailField(_('Email address'), unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=50)
    birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, default="")
    user_type = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.IntegerField()
    owner_id = models.IntegerField()
    content = models.TextField()

class RoomDetails(models.Model):
    id = models.AutoField(primary_key=True)
    roomAddress = models.TextField()
    roomType = models.CharField(max_length=100)
    price = models.IntegerField()
    owner_id = models.IntegerField()
    comment = models.TextField()
    status = models.BooleanField()
    area = models.FloatField(default=0)
    bathroom = models.IntegerField(default=0)
    kitchen = models.IntegerField(default=0)
    air_conditioning = models.IntegerField(default=0)
    balcony = models.IntegerField(default=0)
    waterPrice = models.IntegerField(default=0)
    electricPrice = models.IntegerField(default=0)
    postDate = models.DateField()
    image1 = models.ImageField(upload_to = 'pictures/',default = None)
    image2 = models.ImageField(upload_to = 'pictures/',default = None)
    image3 = models.ImageField(upload_to = 'pictures/',default = None)

class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.IntegerField()
    renter_id = models.IntegerField()
    room_id = models.IntegerField()
    rental_date = models.DateField()
    duration = models.IntegerField()

