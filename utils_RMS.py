import numpy as np

def crear_tablero():
    """
    creamos un tablero por defecto de 10x10 relleno del carácter "_"
    usamos la funcion de numpy
    """
    tablero = np.full((10,10), " ")
    return tablero

def pedir_barcos_jugador():
    #lista_barcos_jugador = [[(0,1), (0,2)], [(3,4),(4,4),(5,4)]]
    pos_inicial_f= int(input("columna"))
    pos_inicial_c= int(input("columna"))
    inicio = [pos_inicial_f, pos_inicial_c]
    print(inicio)
    long = 0
    while long!= 3:
        inicio[long] = long + 1
        print(inicio)
        long += 1

    print(inicio)


def pedir_barcos_rival():
    #randon
    pass


def colocar_barcos (lista_barcos, tablero):
    """
    que recibirá la lista de casillas de un barco y el tablero donde colocarlo. 
    Prueba primero a posicionar un par de barcos por ejemplo en [(0,1), (1,1)] y [(1,3), (1,4), (1,5), (1,6)]. 
    Los barcos serán Os mayúsculas. Como ves, un barco de dos posiciones de eslora y otro de cuatro.

    ¡Mucho ojo con barcos que estén superpuestos 
    (no pueden ocupar dos barcos la misma casilla) o barcos que se salgan del tablero!
    """
    for i in lista_barcos:
        for j in i:
            tablero[j]= "O"
    return tablero


def disparar (tablero,lista):
    """
    si el disparo acierta en un barco sustituye la O por una X (tocado), si es agua, sustituye la _ por una A (Agua)
    """
    fila =int(input("fila: "))
    columna = int(input("columna: ")) 

    if tablero[fila][columna] =="O":
        tablero[fila][columna] = "A"
    else:
        tablero[fila][columna]= "#"

    lista.append((fila, columna))

    return tablero,lista

def crear_barco (eslora):
    eslora = 3
    pos_inicial = (np.random.randint(9),np.random.randint(9))
    orientacion = np.random.choice(["H", "V"]) # choice funcion de letras
    print(orientacion)
    lista_barco = [pos_inicial]
    print(lista_barco)

    pos = pos_inicial

    while len(lista_barco) < eslora:
        if orientacion == "V":
            pos = (pos[0 ]+1, pos[1])
            lista_barco.append(pos)
        else:
            
            pos = (pos[0], pos[1] +1)
            lista_barco.append(pos)

    return lista_barco  

def crear_lista_barcos():
    """
    Crea una lista de casillas de un barco en función a la eslora, de forma aleatoria.
    6 barcos en total:
    -3 barcos de eslora 2. 
    -2 de eslora 3. 
    -1 eslora 4
    """
    lista_esloras = [2,2,2,3,3,4]
    lista_barcos =[]

    for i in lista_esloras:
        barco = crear_barco(i)
        lista_barcos.append(barco)
#comprobar si alguna de las tublas se repite volver a llamar a la funcion

    return lista_barcos