from django.urls import path #Do we need to import path??
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:number>/', views.number),
    path('<int:number>/edit/', views.edit),
    path('<int:number>/delete/', views.delete),

]