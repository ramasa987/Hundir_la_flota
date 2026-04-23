from utils_RMS import crear_tablero, colocar_barcos, pedir_barcos_jugador, disparar, crear_barco, crear_lista_barcos
#VARIABLES JUGADOR
tablero_jugador_disparos = crear_tablero() #tablero donde se marcan los disparos del jugador
tablero_jugador_barcos = crear_tablero() # tablero donde se marcan los barcos del jugador
lista_disparos_jugador =[]

#VARIABLES RIVAL
tablero_rival_disparos = crear_tablero() #tablero donde se marcan los disparos del rival
tablero_rival_barcos = crear_tablero() # tablero donde se marcan los barcos del rival
lista_disparos_rival =[]

#FUNCION DE PEDIR BARCOS AL RIVAL Y JUGADOR
#lista_barcos_jugador = pedir_barcos_jugador()
#lista_barcos_rival = pedir_barcos_rival()

#lista_barcos_jugador = [[(0,1), (0,2)], [(3,4),(4,4),(5,4)]]
#lista_barcos_rival = [[(3,1), (3,2)], [(3,7),(4,7),(5,7)]]

#colocar barcos jugador
tablero_jugador_barcos = colocar_barcos(lista_barcos, tablero_jugador_barcos)
#colocar barcos jugador
tablero_rival_barcos = colocar_barcos(lista_barcos,tablero_rival_barcos)

print(tablero_jugador_disparos)
print("______________________")
print(tablero_jugador_barcos)

#SOY EL RIVAL
tablero_jugador_barcos = disparar(tablero_jugador_barcos, lista_disparos_rival)

print(tablero_jugador_barcos)
print(lista_disparos_rival)

#CREAR BARCO
barco = crear_lista_barcos (4)
    #Crea una lista de casillas de un barco en función a la eslora, de forma aleatoria.
    #6 barcos en total:
    #-3 barcos de eslora 2. 
    #-2 de eslora 3. 
    #-1 eslora 4


