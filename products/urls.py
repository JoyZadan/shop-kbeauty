from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('brands/', views.all_brands, name='brands'),
    path('brand_detail/<int:brand_id>',
         views.brand_detail, name='brand_detail'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit_brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
]
