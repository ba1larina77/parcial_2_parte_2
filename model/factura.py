from datetime import datetime

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.fecha = datetime.now()
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
