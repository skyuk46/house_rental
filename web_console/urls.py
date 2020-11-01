from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('about/', views.about),
   path('login/', views.login),
   path('ownerRegister/', views.ownerRegister),
   path('renterRegister/', views.renterRegister),
]