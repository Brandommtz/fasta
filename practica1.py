import re

Demo = open ("demo.fasta")
readDemo = Demo.read()

print (readDemo)

mapeo = {
    ord("K"): " ",
    ord("S"): "",
    ord("Y"): "",
    ord("M"): "",
    ord("W"): "",
    ord("R"): "",
    ord("D"): "",
    ord("H"): "",
    ord("V"): ""
}

readDemo = readDemo.translate(mapeo)

print(readDemo)

cadena1 = 'ATGAATAATTATAATAAAATTTGGGAAATAATTTTAAATGAACTATCAAAAATTTACAGTGATGAAGTTTTTAAAGAAAC'

resultado = re.search(cadena1, readDemo)

inicio = resultado.start()
fin = resultado.end()

print('cadena1 {} inicio {} fin {}.'.format(cadena1, inicio, fin))

array1 =['Hola', 'Esa', 'Mundo', 'Crear', 'Apio', 'Alga', 'Sed', 'Programacion']
print(array1)

print()

orden = sorted(array1)
print(orden)

array2 = [96, 28, 11, 55, 20, 2015, 500, 630, -10, -1, 200, 96]

band = False
while band== False:
    band = True
    for i in range(len(array2)-1):
        if array2[i] > array2[i+1]:
            aux = array2[i]
            array2[i] = array2[i+1]
            array2[i + 1]= aux
            band = False

        print(array2)