from django.urls import path
from .import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
]
