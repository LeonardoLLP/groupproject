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
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    result = gameOfStones(n)
    fptr.write(result + '\n')
    fptr.close()