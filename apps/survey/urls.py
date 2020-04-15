from django.urls import path #Do we need to import path??
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.newSurvey),
]