from django.contrib import admin
from wishlist.models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'product',
        'date_added',
    )

    ordering = ('-user_profile',)


admin.site.register(Wishlist, WishlistAdmin)
