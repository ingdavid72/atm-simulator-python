# ===================================
# SIMULADOR DE CAJERO AUTOMÁTICO
# ===================================

def mostrar_menu():
    print("\n====== CAJERO AUTOMÁTICO ======")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")

def main():
    saldo = 100000
    historial = []  # Lista para guardar los movimientos

    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("\nError: Por favor ingrese solo números enteros.")
            continue

        # 1. Consultar saldo
        if opcion == 1:
            print(f"\nSu saldo actual es: ${saldo:,.0f}")

        # 2. Depositar dinero
        elif opcion == 2:
            try:
                deposito = float(input("Ingrese el valor a depositar: "))
                if deposito > 0:
                    saldo += deposito
                    historial.append(f"Depósito: +${deposito:,.0f}")
                    print(f"\nDepósito exitoso. Nuevo saldo: ${saldo:,.0f}")
                else:
                    print("\nEl depósito debe ser mayor a $0.")
            except ValueError:
                print("\nMonto inválido.")

        # 3. Retirar dinero
        elif opcion == 3:
            try:
                retiro = float(input("Ingrese el valor a retirar: "))
                if retiro > saldo:
                    print("\nFondos insuficientes.")
                elif retiro <= 0:
                    print("\nEl monto a retirar debe ser mayor a $0.")
                else:
                    saldo -= retiro
                    historial.append(f"Retiro: -${retiro:,.0f}")
                    print(f"\nRetiro exitoso. Nuevo saldo: ${saldo:,.0f}")
            except ValueError:
                print("\nMonto inválido.")

        # 4. Historial de movimientos
        elif opcion == 4:
            print("\n--- HISTORIAL DE MOVIMIENTOS ---")
            if not historial:
                print("No hay movimientos registrados.")
            else:
                for idx, movimiento in enumerate(historial, 1):
                    print(f"{idx}. {movimiento}")

        # 5. Salir
        elif opcion == 5:
            print("\nGracias por utilizar nuestro cajero automático.")
            print("Programa finalizado.")
            break

        else:
            print("\nOpción inválida. Seleccione un número entre 1 y 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
