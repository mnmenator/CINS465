from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('chirps/', views.chirps_json),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('comment/<int:chirp>/', views.comment_view),
    path('profile/<str:name>/', views.profile_view),
    path('chat/select/', views.room_select_view),
    path('chat/<str:room_name>/', views.room_view)
]
