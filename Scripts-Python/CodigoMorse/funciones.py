from datos import codigo_morse

def list_to_str (lista):

    string = ''
    for elemento in lista:
        
        string += str(elemento) + ' '
    return string    

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
    print("*" + ' '*13 +'| TRADUCTOR CÓDIGO MORSE |'+' '*13 +'*')
    print("*" + ' '*52 + '*')
    print("*" + ' '*5 + 'MENU:' + ' '*42 + '*') 
    print("*" + ' '*52 + '*')
    print(
        "*     1. Traducir texto a código morse               *\n" 
        "*     2. Traducir código morse a texto               *\n" 
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

class CodigoMorse:

    def a_morse(self, frase):
        traduccion_conv = ''
        frase = frase.split(" ")

        traduccion_morse = []   
        palabra = []

        # Recorro todas las letras en las palabras.
        for palabras in frase:
            palabra.append(palabras)
            
            for letra in palabras:
                # Reemplazo cada letra del par encontrado en el diccionario y lo agrego a la lista.
                traduccion_morse.append(codigo_morse[letra.lower()])
            
            traduccion_morse.append('/')

        # Elimino el último '/' que haya en el final y convierto el tipo de variable lista a string.
        del(traduccion_morse[len(traduccion_morse)-1]) 

        traduccion_conv = list_to_str(traduccion_morse)  

        return traduccion_conv   


    def a_texto(self, codigo_en_morse):
        '''
        Convierte el codigo morse a texto, 
        requiere un parametro 'codigo_en_morse' como string
        '''
        # Busco si se encuentra algún '/' como separador

        if "/" in codigo_en_morse:
            lista_codigo = codigo_en_morse.split(" / ")
            print("lista código:", lista_codigo)
        else:
            lista_codigo = codigo_en_morse.split(" ")

        lista_morse = []

        for codigo in lista_codigo:
            codigo = codigo.split(" ")
            lista_morse.append(codigo)
        
        """ Recorro el caracter en la lista del codigo morse y
            la reemplazo por la leytra en el diccionario"""
        codigo_traducido = ''

        for palabra in lista_morse:

            for letra in palabra:

                for key, value in codigo_morse.items():
                    if letra == value:
                        codigo_traducido += key

            codigo_traducido += ' '      #Agrego espacios luego de cada palabra

        return codigo_traducido