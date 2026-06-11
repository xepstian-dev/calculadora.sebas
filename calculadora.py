print("=== CALCULADORA PYTHON ===")

while True:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Resultado:", num1 + num2)
    elif opcion == "2":
        print("Resultado:", num1 - num2)
    elif opcion == "3":
        print("Resultado:", num1 * num2)
    elif opcion == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: división por cero")
    elif opcion == "5":
        print("Gracias por usar la calculadora")
        break
    else:
        print("Opción inválida")

    print()
