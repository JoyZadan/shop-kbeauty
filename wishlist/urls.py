from django.urls import path
from .import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist,
         name='add_to_wishlist'),
]
