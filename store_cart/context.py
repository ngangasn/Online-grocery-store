from .cart import StoreCart


def cart(request):
    return {'cart': StoreCart(request)}
