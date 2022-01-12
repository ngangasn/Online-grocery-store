from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<slug:category_slug>/', views.product_list, name='products_sorted_with_category'),
    path('<int:id>/<slug:product_slug>/', views.product, name='product'),
]
