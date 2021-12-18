import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
    pass

if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = "Estudiantes_De_Calificacion/calificaciones.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input("Number of grades: ").strip())

    grades = []
    for _ in range(grades_count):
        grades_item = int(input("Grade: ").strip())

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()