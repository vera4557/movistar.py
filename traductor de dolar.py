def dolares_a_pesos(dolares):
    """
    Convierte una cantidad de dólares a pesos colombianos
    """
    tasa_cambio = 4000  # Tasa de cambio aproximada
    pesos = dolares * tasa_cambio
    return round(pesos, 2)

def pesos_a_dolares(pesos):
    """
    Convierte una cantidad de pesos colombianos a dólares
    """
    tasa_cambio = 4000 # Tasa de cambio aproximada
    dolares = pesos / tasa_cambio
    return round(dolares, 2)

def main():
    while True:
        print("\n=== Conversor de Moneda ===")
        print("1. Dólares a Pesos Colombianos")
        print("2. Pesos Colombianos a Dólares")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == "3":
            print("¡Gracias por usar el conversor!")
            break
            
        if opcion == "1":
            try:
                dolares = float(input("Ingrese la cantidad en dólares: $"))
                pesos = dolares_a_pesos(dolares)
                print(f"${dolares:,.2f} USD = ${pesos:,.2f} COP")
            except ValueError:
                print("Por favor, ingrese un número válido")
                
        elif opcion == "2":
            try:
                pesos = float(input("Ingrese la cantidad en pesos colombianos: $"))
                dolares = pesos_a_dolares(pesos)
                print(f"${pesos:,.2f} COP = ${dolares:,.2f} USD")
            except ValueError:
                print("Por favor, ingrese un número válido")
                
        else:
            print("Opción no válida. Por favor seleccione 1, 2 o 3")

if __name__ == "__main__":
    main()