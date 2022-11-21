from funciones import CodigoMorse, menu

traducir = CodigoMorse()

opcion = menu()

while opcion > 0 and opcion <= 3:

    if opcion == 1:
        texto = input("Introduce texto para traducir a código morse: ")

        codigo = traducir.a_morse(texto)

        print("\nCódigo Morse: ", codigo)

    elif opcion == 2:
        texto = input("Introduce código morse para traducir a texto: ")

        codigo = traducir.a_texto(texto)

        print("\nTexto traducido: ", codigo) 

    elif opcion == 3:
        opcion = 0

    if opcion != 0:
        opcion = menu()           


print("\nFIN DEL PROGRAMA\n")