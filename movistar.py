from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict
class CategoriaCliente(Enum):
    NUEVO = "Nuevo"
    REGULAR = "Regular"
    LEAL = "Leal"
class TipoServicio(Enum):
    FIBRA = "Fibra Óptica"
    POSPAGO = "Plan Pospago"
    PREPAGO = "Plan Prepago"

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
 def actualizar_categoria(self):
        tiempo_cliente = datetime.now() - self.fecha_registro
        if tiempo_cliente > timedelta(days=365):
            self.categoria = CategoriaCliente.LEAL
        elif tiempo_cliente > timedelta(days=180):
            self.categoria = CategoriaCliente.REGULAR

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
        self.puntos_fidelidad += 10  # Suma puntos por cada servicio

 def __init__(self, tipo: TipoServicio, nombre: str, descripcion: str, precio: float):
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.activo = True

  def __init__(self, tipo: str, descripcion: str):
        self.tipo = tipo  # consulta, reclamo, sugerencia
        self.descripcion = descripcion
        self.fecha = datetime.now()
 def __init__(self):
        self.clientes: Dict[str, Cliente] = {}
        self.servicios: List[Servicio] = []
def crear_cliente(self, dni: str, nombre: str, telefono: str, direccion: str) -> bool:
        if dni in self.clientes:
            print("Error: Cliente ya existe")
            return False
        
        self.clientes[dni] = Cliente(dni, nombre, telefono, direccion)
        print(f"Cliente {nombre} registrado exitosamente")
        return True
    
    def obtener_cliente(self, dni: str) -> Cliente:
        return self.clientes.get(dni)
    
    def actualizar_cliente(self, dni: str, nombre: str = None, telefono: str = None, 
                          direccion: str = None) -> bool:
        if dni not in self.clientes:
            print("Error: Cliente no encontrado")
            return False
        
        cliente = self.clientes[dni]
        if nombre: cliente.nombre = nombre
        if telefono: cliente.telefono = telefono
        if direccion: cliente.direccion = direccion
        print("Datos del cliente actualizados")
        return True
    
    def eliminar_cliente(self, dni: str) -> bool:
        if dni not in self.clientes:
            print("Error: Cliente no encontrado")
            return False
        
        del self.clientes[dni]
        print("Cliente eliminado")
        return True
 def crear_servicio(self, tipo: TipoServicio, nombre: str, descripcion: str, 
                      precio: float) -> Servicio:
        servicio = Servicio(tipo, nombre, descripcion, precio)
        self.servicios.append(servicio)
        print(f"Servicio {nombre} creado exitosamente")
        return servicio
    
    def asignar_servicio(self, dni: str, servicio: Servicio) -> bool:
        if dni not in self.clientes:
            print("Error: Cliente no encontrado")
            return False
        
        cliente = self.clientes[dni]
        cliente.agregar_servicio(servicio)
        print(f"Servicio {servicio.nombre} asignado al cliente {cliente.nombre}")
        return True
    
    def ver_servicios_cliente(self, dni: str):
        if dni in self.clientes:
            cliente = self.clientes[dni]
            print(f"\nServicios de {cliente.nombre}:")
            for servicio in cliente.servicios:
                print(f"- {servicio.tipo.value}: {servicio.nombre} (${servicio.precio})")
            print(f"Puntos de fidelidad: {cliente.puntos_fidelidad}")
        else:
            print("Cliente no encontrado")
def registrar_interaccion(self, dni: str, tipo: str, descripcion: str) -> bool:
        if dni not in self.clientes:
            print("Error: Cliente no encontrado")
            return False
        
        interaccion = Interaccion(tipo, descripcion)
        self.clientes[dni].interacciones.append(interaccion)
        print("Interacción registrada")
        return True
    
    def ver_interacciones_cliente(self, dni: str):
        if dni in self.clientes:
            cliente = self.clientes[dni]
            print(f"\nInteracciones de {cliente.nombre}:")
            for interaccion in cliente.interacciones:
                print(f"- {interaccion.fecha}: {interaccion.tipo} - {interaccion.descripcion}")
        else:
            print("Cliente no encontrado")
  def analizar_patron_cliente(self, dni: str) -> dict:
        if dni not in self.clientes:
            return {}
        
        cliente = self.clientes[dni]
        return {
            "categoria": cliente.categoria.value,
            "tiempo_cliente": (datetime.now() - cliente.fecha_registro).days,
            "num_servicios": len(cliente.servicios),
            "puntos_fidelidad": cliente.puntos_fidelidad,
            "num_interacciones": len(cliente.interacciones)
        }
    
    def obtener_clientes_leales(self) -> List[Cliente]:
        return [cliente for cliente in self.clientes.values() 
                if cliente.categoria == CategoriaCliente.LEAL]
    
    def analisis_servicios(self):
        total_servicios = {tipo: 0 for tipo in TipoServicio}
        for cliente in self.clientes.values():
            for servicio in cliente.servicios:
                total_servicios[servicio.tipo] += 1
        
        print("\nAnálisis de Servicios:")
        for tipo, cantidad in total_servicios.items():
            print(f"{tipo.value}: {cantidad} clientes")
            def ejecutar_prueba():
    # Crear sistema
    sistema = SistemaMovistar()
    
    # 1. Crear clientes
    sistema.crear_cliente("12345678", "Juan Pérez", "999888777", "Av. Principal 123")
    sistema.crear_cliente("87654321", "María García", "999777888", "Calle Secundaria 456")
    
    # 2. Crear servicios
    servicio_fibra = sistema.crear_servicio(
        TipoServicio.FIBRA,
        "Fibra 200MB",
        "Internet de fibra óptica de 200MB",
        89.90
    )
    
    servicio_pospago = sistema.crear_servicio(
        TipoServicio.POSPAGO,
        "Plan Ilimitado",
        "Plan con datos ilimitados",
        49.90
    )
    
    # 3. Asignar servicios
    sistema.asignar_servicio("12345678", servicio_fibra)
    sistema.asignar_servicio("12345678", servicio_pospago)
    sistema.asignar_servicio("87654321", servicio_fibra)
    
    # 4. Registrar interacciones
    sistema.registrar_interaccion(
        "12345678",
        "consulta",
        "Consulta sobre velocidad de internet"
    )
    sistema.registrar_interaccion(
        "12345678",
        "reclamo",
        "Problema con la facturación"
    )
    
    # 5. Mostrar información
    print("\n=== RESULTADOS DE LA PRUEBA ===")
    
    # Ver servicios de clientes
    sistema.ver_servicios_cliente("12345678")
    sistema.ver_servicios_cliente("87654321")
    
    # Ver interacciones
    sistema.ver_interacciones_cliente("12345678")
    
    # Ver análisis de servicios
    sistema.analisis_servicios()
    
    # Ver análisis de un cliente
    patron = sistema.analizar_patron_cliente("12345678")
    print("\nAnálisis del cliente Juan Pérez:")
    for key, value in patron.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    ejecutar_prueba()
