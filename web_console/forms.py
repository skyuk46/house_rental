from django import forms
from .models import *
import re
from django.contrib.auth.models import User
import datetime


class RoomDetailsPostForm(forms.ModelForm):

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
    
    roomAddress = forms.CharField(label="Địa chỉ phòng",max_length=150,required=True)
    roomDescription = forms.CharField(max_length = 300,label="Miêu tả phòng")
    roomType = forms.ChoiceField(label='Loại phòng', choices= roomType_choices,required=True)
    price = forms.FloatField(label='Giá thuê',required=True)
    owner_id = forms.IntegerField(label='Mã chủ phòng',required=True)
    status = forms.ChoiceField(label='Tình trạng', choices= status_choices,required=True)
    area = forms.FloatField(label='Diện tích',required=True)
    bathroom = forms.IntegerField(label='Số phòng tắm',required=True)
    bedroom = forms.IntegerField(label='Số phòng ngủ',required=True)
    kitchen = forms.IntegerField(label='Số nhà bếp',required=True)
    air_conditioning = forms.IntegerField(label='Điều hòa',required=True)
    balcony = forms.IntegerField(label='Ban công',required=True)
    waterPrice = forms.IntegerField(label='Giá nước',required=True)
    electricPrice = forms.IntegerField(label='Giá điện',required=True)
    postDate = forms.DateTimeField(label="Ngày đăng",initial=datetime.datetime.now())
    image1 = forms.ImageField(label='Ảnh minh họa 1')
    image2 = forms.ImageField(label='Ảnh minh họa 2')
    image3 = forms.ImageField(label='Ảnh minh họa 3')

    class Meta:
        model = RoomDetails
        #fields = ['productCode','productName', 'productLine','instock','sold','sale','price','description','images','image']
        fields = ('roomAddress','roomDescription','roomType','price','owner_id','status','area','bathroom','bedroom','kitchen','air_conditioning','balcony','waterPrice','electricPrice','postDate','image1','image2','image3') 
        #, use all the fields   

class UserRegisterForm(forms.ModelForm):
    USER_CHOICES =( 
        ("owner", "Người cho thuê"), 
        ("renter", "Người thuê"), 
    ) 

    username = forms.CharField(required=True)
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(),required=True)
    name = forms.CharField(label='Họ tên',max_length=50,required=True)
    birth = forms.DateField(label="Ngày sinh",required=True)
    phone = forms.CharField(label='Số điện thoại',max_length=15,required=True)
    address = forms.CharField(label="Địa chỉ ( Chỉ điền nếu là người cho thuê)",max_length=200)
    user_type = forms.ChoiceField(label="Loại tài khoản",required=True,choices= USER_CHOICES)
    user_id = 1
    if Users.objects.last():
        user_id = Users.objects.last().user_id + 1

    class Meta:
        model = Users
        fields = ('username','email','name','birth','phone','address','user_type','password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if re.search(r'^\w+&', email):
            raise forms.ValidationError("Email có kí tự đặc biệt")
        try:
            Users.objects.get(email = email)
        except Users.DoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại")

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            Users.objects.get(username=username)
        except Users.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        Users.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'], name = self.cleaned_data['name'], birth = self.cleaned_data['birth'], phone = self.cleaned_data['phone'], address = self.cleaned_data['address'], user_type = self.cleaned_data['user_type'])