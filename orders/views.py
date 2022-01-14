from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from store_cart.cart import StoreCart
from .tasks import order_created


def create_order(request):
    cart = StoreCart(request)
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear_cart()
        # order_created.delay(order.id)
        request.session['order_id'] = order.id
        return redirect(reverse('payment:process'))
        # return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})


# add a line
