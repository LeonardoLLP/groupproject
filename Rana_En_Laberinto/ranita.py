import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    for n_itr in range(n):
        row = input()
        # Write your code here
        pass
    for k_itr in range(k):
        second_multiple_input = input().rstrip().split()
        i1 = int(second_multiple_input[0])
        j1 = int(second_multiple_input[1])
        i2 = int(second_multiple_input[2])
        j2 = int(second_multiple_input[3])
        # Write your code here
        pass

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


"""

