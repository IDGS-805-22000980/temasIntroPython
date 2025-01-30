#lista
"""
lista1=[10,5,3]
lista2=[1.5,2.66,1.70,89.2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista1))
print(lista1[0])


x=0
sum=0
while x<len(lista1):
    sum=sum+lista1[x]
    x=x+1

print("La suma es: {}".format(sum))

#Agregar un elemento a la lista
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])


#Pedir elementos a insertar en una lista
lista5=[]
for x in range(5):
    valor=int(input("Ingresa un valor: "))
    lista5.append(valor)
    
print(lista5)


#Eliminar elementos de lista
print(lista1)
lista1.pop()
print(lista1)
"""



"""
Crea un programa que pida una cantidad n de números y almacenarlos en un arreglo
la salida deberá ser la siguiente
Lista completa: xxxxx
Numeros pares de la lista: ppppppp
Numeros impares de la lista: iiiiiii
"""

cant=0
lista=[]
listaPar=[]
listaIn=[]
print("Dame una cantidad de numeros")
cant = int(input(""))

for x in range(cant):
    n=int(input("Ingresa los valores: "))
    lista.append(n)
    

print(lista)
for numero in range(len(lista)):
    if numero % 2 == 0:
        listaPar.append((lista[numero]))
    else:
        listaIn.append(lista[numero])


print("Los números pares son: ",listaPar)
print("Los números inpares son: ",listaIn)


"""
lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)
"""
