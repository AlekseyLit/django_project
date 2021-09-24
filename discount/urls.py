
from django.urls import path
from discount import views

urlpatterns = [
    path('', views.index),
]
