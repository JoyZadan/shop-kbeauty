from django.contrib import admin
from .models import Main_Category, Category, Subcategory, Brand, Product

# Register your models here.


class Main_CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
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
        'price',
        'discount',
        'image'
    )


admin.site.register(Main_Category, Main_CategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
