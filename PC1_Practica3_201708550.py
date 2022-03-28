
import random

contadorPremios = 0  # cantidad de premios disponibles
numParedes = 0
numFantasmas = 0
numPremios = 0
jump = "---------"  # lineas de tablero
puntos = 0  # cantidad de puntos
vida = 1
usuario = ""
tab = []  # arreglo tablero
filas = 7
columnas = 8
teclado = ""  # scanner
x = random.randrange(1, 6)
y = random.randrange(1, 7)


def definirTablero(x, y):  # define el tablero de juego
    for i in range(filas):
        tab.append([])
        for j in range(columnas):
            if j == 0 or j == 7 or i == 0 or i == 6:
                espacio = "|"
                tab[i].append(espacio)
            else:
                espacio = " "
                tab[i].append(espacio)
                tab[i][j] = " "

    tab[5][3] = "X"
    tab[3][1] = "X"
    tab[1][5] = "X"
    tab[2][2] = "X"
    tab[4][1] = "X"
    tab[5][6] = "X"

    tab[1][1] = "@"
    tab[3][2] = "@"
    tab[4][4] = "@"
    tab[5][2] = "@"

    tab[3][3] = "O"
    tab[4][5] = "O"
    tab[2][4] = "O"
    tab[5][5] = "O"

    if tab[x][y] != " ":
        x = random.randrange(1, 6)
        y = random.randrange(1, 7)
        definirTablero(x, y)
    else:
        tab[x][y] = "<"
        menu()


def imprimirTablero(x, y):  # muestra el tablero en consola
    for i in range(filas):
        print()
        for j in range(columnas):
            print(tab[i][j], end=" ")
        print()
    movimientos(x, y)


def movimientos(x, y):
    teclado = input(
        "Muevete con W,A,S,D; para volver al menu de inicio pulsa F: ")
    if teclado == "F" or teclado == "f":
        x = random.randrange(1, 6)
        y = random.randrange(1, 7)
        definirTablero(x, y)
    if teclado == "W" or teclado == "w":
        posicion = x
        tab[posicion ][y] = " "
        posicion  = posicion -1
        if tab[posicion ][y] == "+" or tab[posicion ][y] == "X":
            posicion = posicion +1
            tab[posicion ][y] = "<"
            x = posicion 
            imprimirTablero(x, y)
        else:
            tab[posicion ][y] = "<"
            x = posicion 
            imprimirTablero(x, y)
    elif teclado == "S" or teclado == "s":
        p = x
        tab[posicion][y]  = " "
        posicion  = posicion +1
        if tab[posicion][y] == "+" or tab[posicion][y] == "X":
            posicion  = posicion -1
            tab[posicion][y] = "<"
            x = p
            imprimirTablero(x, y)
        else:
            tab[posicion][y] = "<"
            x = p
            imprimirTablero(x, y)
    elif teclado == "D" or teclado == "d":
            posicion = y
            tab[x][posicion] = " "
            posicion = posicion +1
            if tab[x][posicion ] == "+" or tab[x][posicion] == "X":
                posicion = posicion -1
                tab[x][posicion] = "<"
                y = posicion
                imprimirTablero(x, y)
            else:
                tab[x][posicion] = "<"
                y = posicion
                imprimirTablero(x, y)
    elif teclado == "A" or teclado == "a":
            posicion = y
            tab[x][posicion] = " "
            posicion = posicion-1
            if tab[x][posicion] == "+" or tab[x][posicion] == "X":
                posicion = posicion+1
                tab[x][posicion] = "<"
                y = posicion
                imprimirTablero(x, y)
            else:
                tab[x][posicion] = "<"
                y = posicion
                imprimirTablero(x, y)


def Usuario(usuario, puntos):  # panel de control
    teclado = ""
    print("-------------------------------------------------------------------------------------------------")
    print("USUARIO: "+usuario)
    pts = str(puntos)
    print("PUNTEO: "+pts)
    imprimirTablero(x, y)


def menu():  # menu de inicio
    print("====MENÚ DE INICIO====")
    print("1. Iniciar Juego")
    print("2. Salir")
    teclado = input("Seleccione una opcion: ")
    if teclado == "2":
        print("adios")
        exit()
    else:
        while teclado != "2":
            if teclado == "1":
                print("1")
                teclado = ""
                user = input("Ingrese nombre de Usuario: ")
                usuario = user
                Usuario(usuario, puntos)
                return
            else:
                print("Seleccione una opcion valida")
                teclado = ""
                menu()


definirTablero(x, y)
