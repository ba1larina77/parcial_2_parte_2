from model.producto_control import ProductoDeControl

class ControlDePlagas(ProductoDeControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)
        self.periodo_carencia = periodo_carencia
