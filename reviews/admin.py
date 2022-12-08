from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'content',
        'date',
        'is_featured',
    )

    ordering = ('-date',)


admin.site.register(Review, ReviewAdmin)
