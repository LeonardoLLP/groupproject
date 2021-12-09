import os

def ArraySumaSimple(ar):
    suma=0
    for i in ar:
        suma = suma + i
    return suma

if __name__ =='__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion1.txt', 'w')
    print("Escribe el tamaño de la matriz")
    cuenta_ar = int(input().strip())
    print("Escribe los números separados por un espacio entre cada número")
    ar = list(map(int, input().rstrip().split()))

    resultado = ArraySumaSimple(ar)

    fptr.write(str(resultado),'\n')