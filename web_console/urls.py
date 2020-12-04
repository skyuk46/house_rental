from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('about/', views.about),
   path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
   path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),   
   path('userRegister/', views.userRegister),
   path('RoomPost/',views.RoomPost),
   path('roomDetails/', views.roomDetails),
   path('roomList/',views.roomList),
   path('search/', views.search),
   path('ownerRoomList/',views.ownerRoomList),
   path('userConfirm/',views.userConfirm),
   url(r'^postComment/$',views.postComment),
   path('userProfile/',views.userProfile),
   url(r'^update_rating/$', views.update_rating)
]