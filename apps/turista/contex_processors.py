from . import carrito

def cart(request):
    return {'cart': carrito(request)}
