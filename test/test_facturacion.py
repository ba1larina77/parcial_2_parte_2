import unittest
from model.cliente import Cliente
from model.factura import Factura
from model.producto import Producto

class TestFacturacion(unittest.TestCase):
    def test_crear_cliente(self):
        cliente = Cliente("Juan", "123456")
        self.assertEqual(cliente.nombre, "Juan")
        self.assertEqual(cliente.cedula, "123456")
    
    def test_crear_factura(self):
        cliente = Cliente("Juan", "123456")
        factura = Factura(cliente)
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(factura.total, 0)
    
    def test_agregar_producto_a_factura(self):
        cliente = Cliente("Juan", "123456")
        factura = Factura(cliente)
        producto = Producto("Fertilizante", 10.0)
        factura.agregar_producto(producto)
        self.assertIn(producto, factura.productos)
        self.assertEqual(factura.total, producto.precio)

if __name__ == '__main__':
    unittest.main()
