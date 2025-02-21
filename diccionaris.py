rom datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict

# Enumeraciones para categorías y estados
class CategoriaCliente(Enum):if
    NUEVO = "Nuevo"
    REGULAR = "Regular"
    LEAL = "Leal"

class TipoServicio(Enum):
    FIBRA = "Fibra Óptica"
    POSPAGO = "Plan Pospago"
    PREPAGO = "Plan Prepago"

# Clase para manejar la información del cliente
class Cliente:
    def __init__(self, dni: str, nombre: str, telefono: str, direccion: str):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = datetime.now()
        self.servicios = []
        self.interacciones = []
        self.puntos_fidelidad = 0
        self.categoria = CategoriaCliente.NUEVO
        
    
if __name__ == "__main__":
    ejecutar_prueba()