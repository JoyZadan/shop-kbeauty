from django.urls import path
from .import views

urlpatterns = [
    path('reviews/<int:product_id>', views.reviews, name='reviews'),
]
