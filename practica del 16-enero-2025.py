"""""
Hacer un programa que permita calcular la distancia entre 2 puntos
"""
import math

print("Dame la primer coordenada")
x1 = int (input("Punto 1: "))
y1 = int (input("Punto 2: "))

print("Dame la Segunda coordenada")
x2 = int (input("Punto 1: "))
y2 = int (input("Punto 2: "))

result =int(math.sqrt((x2-x1)**2+(y2-y1)**2))
print(result)

