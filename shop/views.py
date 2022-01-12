from django.shortcuts import render, get_object_or_404

from store_cart.views import cart_detail

from .models import Category, Product
from store_cart.forms import AddProductToCartForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    template_name = 'catalog/products.html'
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, template_name, context)


def product(request, product_slug, id):
    product = get_object_or_404(Product, id=id, slug=product_slug, available=True)
    cart_product_form = AddProductToCartForm()
    template_name = 'catalog/product.html'
    return render(request, template_name, {'product': product, 'cart_product_form': cart_product_form})
