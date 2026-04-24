from utils_r4 import crear_tablero, colocar_barcos, disparar
import time
import numpy as np

print(" vamos a jugar al jego HUNDIR LA FLOTA")
print(" definimos 2 tableros para el jugador")
print(" Un tablero es para disparar y el otro para colocar los barcos")
print(" lo mismo para el rival")

time.sleep(3)

print(" los barcos estan colocados de forma fija")
print(" DISPARA, mucha suerte")

time.sleep(3)

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

print("________TABLERO JUGADOR_DISPASOR_____________")
print(tablero_jugador_barcos)
print("_______TABLERO JUGADOR BARCOS_______________")
print(tablero_rival_barcos)

time.sleep(3)
print("tu turno jugador")



time.sleep(3)

turno_jugador = True
while True:
    if turno_jugador == True:
        #disparo jugador
        tablero_rival_barcos, lista_disparo_jugador, turno_jugador = disparar (tablero_rival_barcos,lista_disparo_jugador,turno_jugador)
        time.sleep(3)
        print("________TABLERO DISPAROS JUGADOR_____________")
        print(tablero_jugador_barcos, turno_jugador)

        print("__________TABLERO RIVAL BARCOS_______________")
        print(tablero_rival_barcos)

    else:
        print("turno jugador")
        break

    pos_o = np.any(tablero_jugador_barcos == "O") #metodo any comprueba la O en cualqueir sitio del aaray
    if "O" == False:
        print("FIN DEL JUEGO")
        break
