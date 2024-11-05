from model.producto_control import ProductoDeControl

class Fertilizante(ProductoDeControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
