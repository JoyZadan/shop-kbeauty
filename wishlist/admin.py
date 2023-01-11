from django.contrib import admin
from wishlist.models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'date_added',
    )
    list_filter = (
        'user_profile',
    )
    search_fields = (
        'user',
        'product',
        'date_added',
    )

    ordering = ('-user_profile',)


admin.site.register(Wishlist)
