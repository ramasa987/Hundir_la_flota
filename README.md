**# Hundir_la_flota**

## Descripción

Este proyecto implementa el juego clásico "Hundir la Flota" en Python. El juego involucra dos jugadores, cada uno con su propio tablero de barcos. El objetivo es hundir todos los barcos del oponente mediante disparos a sus coordenadas.

## Autor

    Raúl Marcos

## Librerías Utilizadas

    NumPy

## Recursos Utilizados

    Python 3.12.10
    VSCode

## Archivos
    utils.py

    Este archivo contiene funciones esenciales para el juego.
    crear tablero un tablero por defecto de 10x10 relleno del carácter "_"
    colcar barcos
    disparar

    main.py

    El script principal inicia y gestiona el juego. El jugador juega contra la maquina.
    La posicion de los barcos esta definida por una lista fija

## Ejecución

    Para iniciar el juego, simplemente ejecute el script main.py. Siga las instrucciones en la consola para ingresar coordenadas y jugar contra la máquina.


## Reglas del Juego

    Cada jugador tiene barcos de diferentes longitudes:
        3 barcos de 2 posiciones de eslora
        2 barcos de 3 posiciones de eslora
        1 barco de 4 posiciones de eslora
    Los jugadores toman turnos para disparar a las coordenadas del oponente.
    El juego solo realiza la funcionde TOCADO o AGUA.
    Las coordenadas se ingresan como pares de números (fila, columna) del 0 al 9.
    

## Salida del Juego

El juego imprime en la consola el resultado del juego.
