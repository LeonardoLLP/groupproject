#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    puntos_a=0
    puntos_b=0
    for i in range(3):
        if (a[i]>b[i]):
            puntos_a=puntos_a+1
        elif(a[i]<b[i]):
            puntos_b=puntos_b+1
        #No hace falta else porque si se da el caso de que sean iguales no hay que hacer nada
    return str(puntos_a)+" "+str(puntos_b)
        

def main():
    os.environ['OUTPUT_PATH'] = 'Comparacion_Lucia_Carlos.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

if __name__ == '__main__':
    main()
