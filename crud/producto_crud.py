from model.control_plagas import ControlDePlagas
from model.fertilizante import Fertilizante
from model.antibiotico import Antibiotico

def crear_control_plagas(nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
    return ControlDePlagas(nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia)

def crear_fertilizante(nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
    return Fertilizante(nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion)

def crear_antibiotico(nombre, precio, dosis, tipo_animal):
    return Antibiotico(nombre, precio, dosis, tipo_animal)
