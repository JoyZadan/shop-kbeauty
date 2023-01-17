from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    # Adds order line items in Django Admin
    # All fields (product name, size and quantity) are editable
    # except LineItemOnly which is a readonly field
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # Order fields specified if readonly or editable
    inlines = (OrderLineItemAdminInline,)

    # readonly fields
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid',)

    # editable fields, displayed in Django admin in the order they appear below
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid',)

    # fields included in the order columns in admin
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # displayed in reverse chronological order
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
