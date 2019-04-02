from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('page/<int:page>/', views.page_view),
    path('helloworld/', views.helloworld),
    path('todo/', views.todo),
    path('todos/', views.todos_json),
    path('chirps/', views.chirps_json),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('comment/<int:chirp>/', views.comment_view),
]
