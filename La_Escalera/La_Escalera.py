#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        #print(" "*(n-i),end="")
        # imprimir blancos
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,i):
            print("#",end="")
        print()

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)