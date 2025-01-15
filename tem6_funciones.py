import os

def funcion1():
    os.system('cls')
    print("Dame 2 numeros: ")
    num1= int(input("Primer numero: "))
    num2= int(input("Segundo numero: "))
    res=num1+num2
    print("la suma de {} y {} es {}".format(num1,num2,res))
    

def funcion2():
    print("Hola soy la función 2")

def run():
    os.system('cls')
    print("Menu de opciones")
    print("1. Suma de dos numeros")
    print("2. Otra opcion")
    print("3. Salir")
    op=int(input("Numero: "))
    if op ==1:
        funcion1()
    else:
        funcion2()


if __name__ == "__main__":
    run()
