import math
import os
import random
import re
import sys

def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        to_next_multiple = 5 - (grades % 5)
        if to_next_multiple < 3 and grades >= 40:
            final_grades.append(grade + to_next_multiple)
        else:
            final_grades.append(grade)

    return final_grades

if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = "Estudiantes_De_Calificacion/calificaciones.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input("Number of grades: ").strip())

    grades = []
    for _ in range(grades_count):
        grades_item = int(input("Grade: ").strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()