from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(default='',max_length=50, unique=True)
    email = models.EmailField(_('Email address'), default='a@gmail.com')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=50,default='A')
    birth = models.DateField(default='2020-11-9')
    phone = models.CharField(max_length=15,default='0214567123')
    address = models.CharField(max_length=200, default="")
    user_type = models.CharField(max_length=20,default='admin')

    def __str__(self):
        return self.email

class WaitingList(models.Model):
    username = models.CharField(default='',max_length=50, unique=True)
    email = models.EmailField(_('Email address'), default='a@gmail.com')
    password = models.CharField(default='',max_length=100)
    name = models.CharField(max_length=50,default='A')
    birth = models.DateField(default='2020-11-9')
    phone = models.CharField(max_length=15,default='0214567123')
    address = models.CharField(max_length=200, default="")
    user_type = models.CharField(max_length=20,default='admin')

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.IntegerField()
    owner_id = models.IntegerField()
    content = models.TextField()

class RoomDetails(models.Model):
    status_choices = (
        ('Chưa cho thuê','Available'),
        ('Đã cho thuê','notAvailable')
    )
    roomType_choices = (
        ('Phòng trọ','Phòng trọ'),
        ('Chung cư mini','Chung cư mini'),
        ('Chung cư','Chung cư'),
        ('Nhà nguyên căn','Nhà nguyên căn')
    )
    
    id = models.AutoField(primary_key=True)
    roomAddress = models.CharField(max_length=150,default="")
    roomDescription = models.TextField(default="(Không có mô tả)")
    roomType = models.CharField(max_length=100, choices= roomType_choices)
    price = models.FloatField()
    owner_id = models.IntegerField()
    status = models.CharField(max_length=20, choices= status_choices)
    area = models.FloatField(default=0)
    bathroom = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=0)
    air_conditioning = models.IntegerField(default=0)
    balcony = models.IntegerField(default=0)
    waterPrice = models.IntegerField(default=0)
    electricPrice = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
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

class Comment(models.Model):
    room_id = models.SmallIntegerField()
    author = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class WaitingComment(models.Model):
    id = models.AutoField(primary_key=True)
    room_id = models.SmallIntegerField()
    author = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField()

class Rating(models.Model):
    id = models.AutoField(primary_key = True)
    room_id = models.SmallIntegerField()
    rating = models.CharField(default='',max_length=10)
    rater = models.CharField(max_length=50,default="")

class Message(models.Model):
    id = models.AutoField(primary_key = True)
    receiver = models.CharField(max_length=50)
    sender = models.CharField(max_length=50)
    message = models.TextField()
    send_date = models.DateTimeField()

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    room_id = models.IntegerField()