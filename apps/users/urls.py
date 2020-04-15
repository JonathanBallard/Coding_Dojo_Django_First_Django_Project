from django.urls import path #Do we need to import path??
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('users/new/', views.newUser),
    path('users/', views.users),

]