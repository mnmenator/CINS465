from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('page/<int:page>/', views.page_view),
    path('helloworld', views.helloworld)
]
