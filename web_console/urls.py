from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('about/', views.about),
   path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),   
   path('userRegister/', views.userRegister),
   path('upload_post/',views.uploadPost),
   path('RoomPost/',views.RoomPost)
]