import numpy as np

def crear_tablero():
    """
    creamos un tablero por defecto de 10x10 relleno del carácter "_"
    """
    
    tablero = np.full((10,10),"_")
    return tablero

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


def disparar (tablero,lista,turno):
    """
    si el disparo acierta en un barco sustituye la O por una X (tocado), si es agua, sustituye la _ por una A (Agua)
    """
    fila =int(input("fila: "))
    columna = int(input("columna: "))
    print(fila,columna)
    if tablero[fila][columna] =="O":
        tablero[fila][columna] = "X"
        print("TOCADOOOO !!!!!")
        turno = True
    else:
        tablero[fila][columna]= "A"
        print ("AGUAAAA !!!!")
        turno= False

    lista.append((fila, columna))

    return tablero,lista,turno

