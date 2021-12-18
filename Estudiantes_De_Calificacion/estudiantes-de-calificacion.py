import math
import os
import random
import re
import sys

def gradingStudents(grades):
    if grades % 5 < 3 and grades >= 40:
        return grades + (grades % 5)
    else:
        return grades

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