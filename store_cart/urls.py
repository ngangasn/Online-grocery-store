from django.urls import path

from . import views

app_name = 'store_cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_items_to_cart, name='add_items_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_item_from_cart'),
]
