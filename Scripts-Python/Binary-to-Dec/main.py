from funciones import bintodec, dectobin, menu

opcion = menu()

while opcion > 0 and opcion <= 3:

    if opcion == 1:

        num = int(input("Ingrese un número binario para traducirlo a decimal: "))

        decimal = bintodec(num)

        print("\nNúmero binario: ", num, "Número decimal: ", decimal, "\n\n")

    elif opcion == 2:    
        num = int(input("Ingrese un número para pasarlo a binario: "))

        binario = dectobin(num)

        print("Número base 10: ", num, " y número base 2(binario): ", binario)  

    elif opcion == 3:
        opcion = 0

    if opcion != 0:
        opcion = menu()    

print("\nFIN DEL PROGRAMA\n")        