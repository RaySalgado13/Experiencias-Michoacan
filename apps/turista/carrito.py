from decimal import Decimal
from django.conf import settings
from apps.home.models import Producto

class Carro(object):

    def __init__(self, request):
        # Iniciamos el carro

        self.session = request.session
        carro = self.session.get(settings.CARRO_SESSION_ID)
        if not carro:
            # guarda un carro vacio en la sesion
            carro = self.session[settings.CARRO_SESSION_ID] = {}
        self.carro = carro


    def add(self, producto, cantidad, update_cantidad=False):
        # Añadir un producto al carro o actulizar la cantidad

        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {'cantidad':0,
                                        'precio': str(producto.precio)}
        if update_cantidad:
            self.carro[producto_id]['cantidad'] = cantidad
        else:
            self.carro[producto_id]['cantidad']  += cantidad
        self.save()


    def save(self):
        self.session.modified = True


    def remove(self, producto):
        # Remover un producto del carro

        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.save()

    def __iter__(self):
        #Ingresa a la base de datos para obtener los productos

        producto_ids = self.carro.keys()
        #obtiene el objeto de producto y lo añade al carro
        productos = Producto.objects.filter(id__in=producto_ids)

        carro = self.carro.copy()
        for producto in productos:
            carro[str(producto.id)]['producto'] = producto

        for item in carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        #Cuenta los items del carrito
        return sum(item['cantidad'] for item in self.carro.values())

    def obt_precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())

    def limpia(self):
        #limpia el carro de la sesion
        del self.session[settings.CARRO_SESSION_ID]
        self.save()