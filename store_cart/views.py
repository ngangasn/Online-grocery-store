from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import StoreCart
from .forms import AddProductToCartForm



@require_POST
def add_items_to_cart(request, product_id):
    cart = StoreCart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductToCartForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.addItems(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('store_cart:cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = StoreCart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_product(product)
    return redirect('store_cart:cart_detail')


def cart_detail(request):
    cart = StoreCart(request)
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(initial={'quantity': item['quantity'], 'override':True})
    return render(request, 'cart/detail.html', {'cart': cart})
