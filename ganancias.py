def calcular_ganancias_camisas():
    # Constantes
    PRECIO_COMPRA = 5000
    PRECIO_VENTA = 80000
    GANANCIA_POR_CAMISA = PRECIO_VENTA - PRECIO_COMPRA
    INVENTARIO_INICIAL = {
        'M': 8,
        'L': 8,
        'XL': 8,
    }

    # Función para validar entrada
    def validar_cantidad(talla, cantidad):
        if cantidad > INVENTARIO_INICIAL[talla]:
            return False
        return True

    # Inicializar variables
    total_vendidas = 0
    ganancias_totales = 0
    inventario_actual = INVENTARIO_INICIAL.copy()

    print("\n=== Calculadora de Ganancias de Camisas ===")
    print("Inventario disponible:")
    for talla, cantidad in inventario_actual.items():
        print(f"Talla {talla}: {cantidad} unidades")

    # Solicitar ventas por talla
    for talla in ['M', 'L', 'XL']:
        while True:
            try:
                vendidas = int(input(f"\nIngrese cantidad de camisas talla {talla} vendidas: "))
                if validar_cantidad(talla, vendidas):
                    inventario_actual[talla] -= vendidas
                    total_vendidas += vendidas
                    break
                else:
                    print(f"Error: Solo hay {INVENTARIO_INICIAL[talla]} camisas talla {talla} disponibles")
            except ValueError:
                print("Por favor ingrese un número válido")

    # Calcular ganancias
    ganancias_totales = total_vendidas * GANANCIA_POR_CAMISA

    # Mostrar resultados
    print("\n=== Resumen de Ventas ===")
    print(f"Total de camisas vendidas: {total_vendidas}")
    print(f"Ganancia por camisa: ${GANANCIA_POR_CAMISA:,}")
    print(f"Ganancias totales: ${ganancias_totales:,}")
    print("\nInventario restante:")
    for talla, cantidad in inventario_actual.items():
        print(f"Talla {talla}: {cantidad} unidades")

if __name__ == "__main__":
    calcular_ganancias_camisas()