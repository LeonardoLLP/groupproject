import math
import os
import random
import re
import sys
# if __name__ == '__main__':

first_multiple_input = input("Rows, columns and tunels: ").rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
# k = int(first_multiple_input[2])

#! ---Start--- Board setup
# Legend
print("#: Obstacle")
print("A: Start")
print("M: Mine")
print("%: Exit")
print("W: Free space")

possibilities = ["#", "A", "M", "%"]

board = []
board.append(["#" for _ in range(m + 2)])

#* Adding rows
for n_itr in range(n):
    row_list = input("Type row: ").rstrip().casefold().split(maxsplit = m)
    row_obstacles = []

    row_obstacles.append("#")
    for space in row_list:
        if space in possibilities:
            row_obstacles.append(space)
        else:
            row_obstacles.append("")

    row_obstacles.append("#")

    board.append(row_obstacles)


board.append(["#" for _ in range(m + 2)])

# Print board
for row in board:
    print("[", end="")
    for index in range(len(row)):
        if index != len(row) - 1:
            print("{:6}".format("\'" + row[index] + "\', "), end="")
        else:
            print("{:6}".format("\'" + row[index] + "\'"), end="")
    print("]")

#! ---End--- Board setup


# for k_itr in range(k):
#     second_multiple_input = input().rstrip().split()
#     i1 = int(second_multiple_input[0])
#     j1 = int(second_multiple_input[1])
#     i2 = int(second_multiple_input[2])
#     j2 = int(second_multiple_input[3])
#     # Write your code here
#     pass

# Write your code here

"""Tengo una idea para que esto funcione pero está mmuy loca. Intentaré explicarla.

La ranita se mueve al azar a cada una de sus casillas adyacentes posibles. Lo que vamos a hacer es ir anotando:

1. Las casillas por las que pasa
2. Las diferentes probabilidades que hay de que llegue allí
3. Las casillas que está probando en un momento determinado.

A medida que va progresando, la rana volverá a casilla que ha probado. Entonces, anotará la probabilidad que tenía en ese momento de llegar ahí y eliminará ese arbol.

La rana seguirá y llegará a una mina o a una salida. En ese momento se detiene ese arbol.

Se comprueba entonces la probabilidad de llegar a una mina o a la salida y ya está.

20 veces más complicado de lo que suena.


Por ahora, obviaremos repeticiones de casillas. La rana no puede volver a su misma casilla.

Sería como no haber empezado, y como puede pasar con cada casilla, lo obviamos. Sin embargo, incluimos ir a una casilla de otro camino como válido, sumando la probabilidad
del camino del que venimos.


Opción dos: hacer muchas simulaciones y hallar dividir salidas / simulaciones.

Probablemente lo más razonable de hacer dado que hay que entregarlo en unas horas.
"""

