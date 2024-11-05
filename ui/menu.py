from crud.cliente_crud import crear_cliente, buscar_cliente_por_cedula
from crud.factura_crud import crear_factura, agregar_producto_a_factura
from crud.producto_crud import crear_control_plagas, crear_fertilizante, crear_antibiotico

def mostrar_menu():
    print("1. Registrar cliente")
    print("2. Registrar venta de producto")
    print("3. Buscar cliente por cédula")
    # Agregar más opciones según sea necesario
