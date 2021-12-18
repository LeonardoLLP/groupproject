import math
import os
import random
import re
import sys

# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
# 1. INTEGER s
# 2. INTEGER t
# 3. INTEGER a
# 4. INTEGER b
# 5. INTEGER_ARRAY apples
# 6. INTEGER_ARRAY oranges

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    pass

if __name__ == '__main__':
    first_multiple_input = input("House x1 and x2: ").rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input("Appler and oranger: ").rstrip().split()  #! XD
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    apples = list(map(int, input("Apples: ").rstrip().split()))
    oranges = list(map(int, input("Oranges: ").rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)