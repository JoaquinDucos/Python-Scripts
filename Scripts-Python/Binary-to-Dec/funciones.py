def dectobin (num):
    i = 0
    bin = ''
    resto = 0
    aux = num

    while aux >= 1:
        aux = aux // 2
        i +=1
    
    while num >= 1:
        resto = num % 2
        bin = str(bin) + str(resto)
        i -=1
        num = num // 2

    bin = bin[::-1]
    bin = int(bin)
    return bin

def bintodec (num):
    dec = 0
    contBin = 1
    j = 0
    restoStr = str(num)
    restoStr = restoStr[::-1]

    while num >= 1:
        if int(restoStr[j]) == 1:
            dec += contBin
        j += 1
        num = num // 10
        contBin *= 2

    return dec

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
        "*     1. Traducir código binario a número decimal    *\n" 
        "*     2. Traducir número decimal a código binario    *\n" 
        "*     3. Salir                                       *")
    print("*" + ' '*52 + '*')   
    print("*"*54 +'\n')    

    n=None

    while n==None:

        try :

            n=input("\nSeleccione la opción que desea realizar: ")
            n=int(n)

            while n > 3 or n < 1:

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