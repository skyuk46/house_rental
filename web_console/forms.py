from django import forms
from .models import *
import re
from django.contrib.auth.models import User


class RoomDetailsPostForm(forms.ModelForm):

    class Meta:
        model = RoomDetails
        #fields = ['productCode','productName', 'productLine','instock','sold','sale','price','description','images','image']
        fields = '__all__' 
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

    def save(self):
        Users.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'], name = self.cleaned_data['name'], birth = self.cleaned_data['birth'], phone = self.cleaned_data['phone'], address = self.cleaned_data['address'], user_type = self.cleaned_data['user_type'])