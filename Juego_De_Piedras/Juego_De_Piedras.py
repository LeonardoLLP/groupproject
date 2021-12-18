#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'gameOfStones' function below.

# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.

def gameOfStones(n):
    # Vamos a emplear un método regresivo
    # Como tenemos los cinco primeros valores, crearemos una lista con los valores iniciales que nos ha proporcionado el documento.
    # Cada valor comprobará los índice
    # Si en alguno puede ganar, gana

    # Valores iniciales
    values = [2, 1, 1, 1, 1]

    #! HOW I FOUND THE TRICK:
    # if n >= 6:
    #     for i in range(5, n):
    #         values_to_check = [values[i-j] for j in [2, 3, 5]]
    #         if 2 in values_to_check:  # Después de un movimiento el jugador uno es como el jugador dos: si puede llegar a una situación en la que el jugador dos gana, entonces gana
    #             values.append(1)
    #         else:
    #             values.append(2)

    if n % 7 in [0, 1]:
        return "Player 2 won the game"
    else:
        return "Player 1 won the game"

    print(values)

    if values[n-1] == 1:
        return "Player 1 won the game"
    else:
        return "Player 2 won the game"

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "Juego_De_Piedras/juego-piedas.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()