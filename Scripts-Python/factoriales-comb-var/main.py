from funciones import *

print("\n           COMIENZO DE PROGRAMA\n")

opcion = menu()

while opcion > 0 and opcion <= 3:

    if opcion == 1:
       print("\nNúmero factorial\n")
       n = int (input("Introduce un número (positivo) para saber su factorial: "))
   
       fact = factorial(n)
       print("\nEl factorial de", n, " es: ", fact)

    elif opcion == 2:

        print("\nCombinaciones de M tomadas a N\n")
    
        m = int(input("Introduce M: "))
        n = int(input("Introduce N: "))
    
        comb = combinacion(m,n)
        var = variaciones(m, n)
    
        print("\nCombinación: ", comb)

    elif opcion == 3:

        print("\nVariaciones de M tomadas a N\n")
        m = int(input("Introduce M: "))
        n = int(input("\nIntroduce N: "))

        print("\nVariaciones: : ", var)

    elif opcion == 4:
        opcion = 0

    if opcion != 0:
        opcion = menu()    
    
    
print("\n\n           FIN DE PROGRAMA\n\n") 