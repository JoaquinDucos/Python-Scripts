def factorial (n):
    i = 1
    suma = n
    while( i < n):
        suma *= i
        i += 1
    return suma

def combinacion (m, n):
    comb = ( factorial(m) / ( factorial((m-n)) * factorial(n)) )

    return comb

def variaciones (m, n):
    var = ( factorial(m) / factorial((m-n)) )

    return var

def es_numero(c):

    c = str(c)
    for letra in c:
        if ( letra < chr(48) or letra > chr(57) ):
            return False
    
    return True    

def menu():
    print('\n')
    print('*'*54)
    print("*" + ' '*52 +'*')
    print("*" + ' '*12 +'| TRADUCTOR CÓDIGO BINARIO |'+' '*12 +'*')
    print("*" + ' '*52 + '*')
    print("*" + ' '*5 + 'MENU:' + ' '*42 + '*') 
    print("*" + ' '*52 + '*')
    print(
        "*     1. Permutación de número a factorial           *\n" 
        "*     2. Variación de M tomados de a N               *\n" 
        "*     3. Combinación de M tomados de a N             *\n" 
        "*     4. Salir                                       *")
    print("*" + ' '*52 + '*')   
    print("*"*54 +'\n')    

    n=None

    while n==None:

        try :

            n=input("\nSeleccione la opción que desea realizar: ")
            n=int(n)

            while n > 4 or n < 1:

                print("\nValor fuera de rango\n")
                n= int(input("\nIntente nuevamente: "))

                while not es_numero(n):

                    print("\nIngrese un número por favor.")
                    n= int(input("\nIntente nuevamente: "))
            print('\n')
        except TypeError and ValueError: 
            print("\nLas opciones estan designadas por números.\n\n")
            n = None

    return n

