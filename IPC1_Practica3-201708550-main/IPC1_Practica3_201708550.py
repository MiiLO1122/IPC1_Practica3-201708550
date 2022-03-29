
import random

jump = "-------------"  # lineas de tablero
puntos = 0  # cantidad de puntos
vida = 1
usuario = ""
tab = []  # arreglo tablero
filas = 7
columnas = 8
teclado = ""  # scanner
x = random.randrange(1, 6)
y = random.randrange(1, 7)


def Usuario(usuario, puntos):  # panel de control
    imprimirTablero(x, y, vida, usuario, puntos)


def definirTablero(x, y, vida, usuario, puntos):  # define el tablero de juego
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
        definirTablero(x, y, vida, usuario, puntos)
    else:
        tab[x][y] = "<"
        menu()


def imprimirTablero(x, y, vida, usuario, puntos):  # muestra el tablero en consola
    print("-------------------------------------------------------------------------------------------------")
    print("USUARIO: ", usuario)
    print("PUNTEO: ", puntos)
    for i in range(filas):
        print()
        for j in range(columnas):
            print(tab[i][j], end=" ")
        print()
    movimientos(x, y, vida, usuario, puntos)


def movimientos(x, y, vida, usuario, puntos):
    while vida != 0:
        teclado = input(
            "Muevete con W,A,S,D; para volver al menu de inicio pulsa F: ")
        if teclado == "W" or teclado == "w":
            p = x
            tab[p][y] = " "
            p = p-1
            if tab[p][y] == "|" or tab[p][y] == "X":
                p = p+1
                tab[p][y] = "<"
                x = p
                imprimirTablero(x, y, vida, usuario, puntos)
            elif tab[p][y] == "@":
                vida = 0
                tab[p][y] = "<"
                imprimirTablero(x, y, vida, usuario, puntos)
                print()
                print("Perdiste ja")
                print("Te quedan: ", vida, " vidas")
                print(jump)
                definirTablero(x, y, vida, usuario, puntos)
            elif tab[p][y] == "O":
                v = puntos
                v = v+10
                puntos = v
                tab[p][y] = "<"
                x = p
                if puntos == 50:
                    print("Felicidades ganaste CTM!")
                    print(jump)
                    definirTablero(x, y, vida, usuario, puntos)
                else:
                    imprimirTablero(x, y, vida, usuario, puntos)
            else:
                tab[p][y] = "<"
                x = p
                imprimirTablero(x, y, vida, usuario, puntos)
        elif teclado == "S" or teclado == "s":
            p = x
            tab[p][y] = " "
            p = p+1
            if tab[p][y] == "|" or tab[p][y] == "X":
                p = p-1
                tab[p][y] = "<"
                x = p
                imprimirTablero(x, y, vida, usuario, puntos)
            elif tab[p][y] == "@":
                vida = 0
                tab[p][y] = "<"
                imprimirTablero(x, y, vida, usuario, puntos)
                print()
                print("Perdiste ja")
                print("Te quedan: ", vida, " vidas")
                print(jump)
                definirTablero(x, y, vida, usuario, puntos)
            elif tab[p][y] == "O":
                v = puntos
                v = v+10
                puntos = v
                tab[p][y] = "<"
                x = p
                if puntos == 50:
                    print("Felicidades ganaste CTM!")
                    print(jump)
                    definirTablero(x, y, vida, usuario, puntos)
                else:
                    imprimirTablero(x, y, vida, usuario, puntos)
            else:
                tab[p][y] = "<"
                x = p
                imprimirTablero(x, y, vida, usuario, puntos)
        elif teclado == "D" or teclado == "d":
            p = y
            tab[x][p] = " "
            p = p+1
            if tab[x][p] == "|" or tab[x][p] == "X":
                p = p-1
                tab[x][p] = "<"
                y = p
                imprimirTablero(x, y, vida, usuario, puntos)
            elif tab[x][p] == "@":
                vida = 0
                tab[x][p] = "<"
                imprimirTablero(x, y, vida, usuario, puntos)
                print()
                print("Perdiste ja")
                print("Te quedan: ", vida, " vidas")
                print(jump)
                definirTablero(x, y, vida, usuario, puntos)
            elif tab[x][p] == "O":
                v = puntos
                v = v+10
                puntos = v
                tab[x][p] = "<"
                y = p
                if puntos == 50:
                    print("Felicidades ganaste CTM!")
                    print(jump)
                    definirTablero(x, y, vida, usuario, puntos)
                else:
                    imprimirTablero(x, y, vida, usuario, puntos)
            else:
                tab[x][p] = "<"
                y = p
                imprimirTablero(x, y, vida, usuario, puntos)
        elif teclado == "A" or teclado == "a":
            p = y
            tab[x][p] = " "
            p = p-1
            if tab[x][p] == "|" or tab[x][p] == "X":
                p = p+1
                tab[x][p] = "<"
                y = p
                imprimirTablero(x, y, vida, usuario, puntos)
            elif tab[x][p] == "@":
                vida = 0
                tab[x][p] = "<"
                imprimirTablero(x, y, vida, usuario, puntos)
                print()
                print("Perdiste ja")
                print("Te quedan: ", vida, " vidas")
                print(jump)
                definirTablero(x, y, vida, usuario, puntos)
            elif tab[x][p] == "O":
                v = puntos
                v = v+10
                puntos = v
                tab[x][p] = "<"
                y = p
                if puntos == 50:
                    print("Felicidades ganaste CTM!")
                    print(jump)
                    definirTablero(x, y, vida, usuario, puntos)
                else:
                    imprimirTablero(x, y, vida, usuario, puntos)
            else:
                tab[x][p] = "<"
                y = p
                imprimirTablero(x, y, vida, usuario, puntos)
        elif teclado == "F" or teclado == "f":
            x = random.randrange(1, 6)
            y = random.randrange(1, 7)
            print(jump)
            definirTablero(x, y, vida, usuario, puntos)


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


definirTablero(x, y, vida, usuario, puntos)
