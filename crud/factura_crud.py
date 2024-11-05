from model.factura import Factura

def crear_factura(cliente):
    return Factura(cliente)

def agregar_producto_a_factura(factura, producto):
    factura.agregar_producto(producto)
