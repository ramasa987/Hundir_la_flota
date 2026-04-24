from utils_r5 import crear_tablero, colocar_barcos, disparo_jugador,disparo_rival
import time
import numpy as np

print(" Vamos a jugar al juego HUNDIR LA FLOTA")
print(" Definimos 2 TABLEROS")
print(" TABLERO JUGADOR BARCOS. El jugador coloca sus barcos con una lista fija")
print(" TABLERO RIVAL BARCOS. La maquina coloca sus barcos con una lista fija")

time.sleep(10)

print(" Cuando disparemos, se marcaran en otro tablero para que no repitamos coordenada de disparo")

time.sleep(3)

print(" !!!IMPORT !!! . Los barcos estan colocados de forma fija")
print(" DISPARA, Mucha suerte !!!!!!")

time.sleep(6)

#VARIABLES JUGADOR
tablero_jugador_disparos = crear_tablero() #tablero donde se marcan los disparos del jugador
tablero_jugador_barcos = crear_tablero() # tablero donde se marcan los barcos del jugador


#VARIABLES RIVAL
tablero_rival_disparos = crear_tablero() #tablero donde se marcan los disparos del rival
tablero_rival_barcos = crear_tablero() # tablero donde se marcan los barcos del rival


#lista barcos
lista_barcos_jugador = [[(0,1), (0,2)], [(3,4),(4,4),(5,4)]] #coloca 1 barco en Horizontal otro barco vertical
lista_barcos_rival = [[(3,1), (3,2)], [(3,7),(4,7),(5,7)]]

#LISTA DE DISPAROS
lista_disparo_jugador = []
lista_disparo_rival = []


#colocar barcos jugador
tablero_jugador_barcos = colocar_barcos(lista_barcos_jugador, tablero_jugador_barcos)
#colocar barcos jugador
tablero_rival_barcos = colocar_barcos(lista_barcos_rival, tablero_rival_barcos)

print("________TABLERO JUGADOR_BARCOS_____________")
print(tablero_jugador_barcos)
print("_______TABLERO RIVAL BARCOS_______________")
print(tablero_rival_barcos)

time.sleep(3)
print("tu turno jugador")



time.sleep(3)

turno_jugador = True
while True:
    if turno_jugador == True:
        #disparo jugador
        tablero_rival_barcos, lista_disparo_jugador, turno_jugador = disparo_jugador (tablero_rival_barcos,lista_disparo_jugador,turno_jugador)
        time.sleep(3)
        print("________TABLERO DISPAROS RIVAL_____________")
        print(tablero_jugador_barcos, turno_jugador)

        print("__________TABLERO DISPAROS JUGADOR_______________")
        print(tablero_rival_barcos)

    else:
        print("turno jugador")
        break

    pos_o = np.any(tablero_jugador_barcos == "O") #metodo any comprueba la O en cualqueir sitio del aaray
    if "O" == False:
        print("FIN DEL JUEGO")
        break


turno_rival = True
while True:
    if turno_rival == True:
        #disparo jugador
        tablero_juador_barcos, lista_disparo_rival, turno_rival = disparo_rival (tablero_jugador_barcos,lista_disparo_rival,turno_rival)
        time.sleep(3)
        print("________TABLERO DISPAROS RIVAL_____________")
        print(tablero_rival_barcos, turno_jugador)

        print("__________TABLERO DISPAROS JUGADOR_______________")
        print(tablero_rival_barcos)

    else:
        print("turno rival")
        break

    pos_o = np.any(tablero_rival_barcos == "O") #metodo any comprueba la O en cualqueir sitio del aaray
    if "O" == False:
        print("FIN DEL JUEGO")
        break