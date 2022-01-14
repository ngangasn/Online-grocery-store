from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import related
from shop.models import Product
from accounts.customer import Customer


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('created', )

    def __str__(self): 
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(id=customer_id).order_by('-created')
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity   