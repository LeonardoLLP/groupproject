#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
def aVeryBigSum(ar):
    

def main():
    os.environ['OUTPUT_PATH'] = 'Suma_Muy_Grande.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()


if __name__ == '__main__':
    main()
