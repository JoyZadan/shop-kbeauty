from django.contrib import admin
from .models import Main_Category, Category, Subcategory, Brand, Product

# Register your models here.

admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Product)
