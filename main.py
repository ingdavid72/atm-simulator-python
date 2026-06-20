# ===================================
# SIMULADOR DE CAJERO AUTOMÁTICO
# ===================================

saldo = 100000

while True:

    print("\n====== CAJERO AUTOMÁTICO ======")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    # Consultar saldo
    if opcion == 1:
        print("\nSu saldo actual es: $", saldo)


    # Depositar dinero
    elif opcion == 2:
        deposito = int(input("Ingrese el valor a depositar: "))

        if deposito > 0:
            saldo += deposito
            print("\nDepósito realizado correctamente")
            print("Nuevo saldo: $", saldo)
        else:
            print("El valor del depósito no es válido")


    # Retirar dinero
    elif opcion == 3:
        retiro = int(input("Ingrese el valor a retirar: "))

        if retiro > saldo:
            print("\nFondos insuficientes")
        
        elif retiro <= 0:
            print("\nValor de retiro inválido")

        else:
            saldo -= retiro
            print("\nRetiro realizado correctamente")
            print("Nuevo saldo: $", saldo)


    # Salir
    elif opcion == 4:
        print("\nGracias por utilizar el cajero")
        print("Programa finalizado")
        break


    else:
        print("\nOpción inválida, intente nuevamente")