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
    path('delete-chirp/<int:chirp>/', views.delete_chirp_view),
    path('delete-comment/<int:comment>/', views.delete_comment_view),
    path('chat/select/', views.room_select_view),
    path('chat/<str:room_name>/', views.room_view),
    path('change-friend/<str:operation>/<int:user>/', views.change_friends)
]
