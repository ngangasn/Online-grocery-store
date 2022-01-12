from django.contrib import admin

from .customer import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'address', 'postal_code', 'city',]

