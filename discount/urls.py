
from django.urls import path
from discount import views

urlpatterns = [
    path('', views.index),
    path('discounts', views.discounts, name="discounts"),
    path('offers', views.offers, name="offers"),
    path('contacts', views.contacts, name="contacts"),
    path('account/login', views.login, name="login"),
    path('account/check_user', views.check_user, name="check_user")
]
