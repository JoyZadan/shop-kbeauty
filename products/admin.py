from django.contrib import admin
from .models import MainCategory, Category, Subcategory, Brand, Product

# Register your models here.


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'slug',
        'main_category',
    )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'slug',
        'description',
        'is_featured',
        'image',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'total_quantity',
        'availability',
        'original_price',
        'price',
        'discount',
        'image'
    )


admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
