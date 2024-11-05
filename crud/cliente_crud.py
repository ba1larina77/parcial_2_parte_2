from model.cliente import Cliente

def crear_cliente(nombre, cedula):
    return Cliente(nombre, cedula)

def buscar_cliente_por_cedula(clientes, cedula):
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None
