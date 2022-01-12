from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'customer', 'email', 'address', 'postal_code', 'city', 'paid', 'amount', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]

    def amount(self, instance):
        return instance.get_total_cost()
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(OrderAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['customer'].widget.can_add_related = False
        return form
