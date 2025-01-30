# Luis Eduardo Silva Aguirre.
# Ingeniería en Desarrollo y Gestión de Software 805.
# Cinepolis by Python.

from io import open
import os

class Personas:
    def __init__(self):
        self.historial = []
    
    def excesoBoletos(self, pers, boletos, nombre):
        opcion = int(input("¿Quieres agregar más personas o comprar menos boletos? (1. persona / 2. boletos): "))
        if opcion == 1:
            agregarPersonas = int(input("¿Cuántas personas más serán agregadas? "))
            maxBoletos = (agregarPersonas + pers) * 7
            print("Ahora puedes comprar hasta {} boletos.".format(maxBoletos))
            boletos = int(input("¿Cuántos boletos deseas comprar? "))
            if boletos > maxBoletos:
                print("Aún superas el límite de boletos.")
            else:
                self.calcularTotal(boletos, nombre)
        elif opcion == 2:
            boletos = int(input("¿Cuántos boletos deseas comprar ahora? "))
            maxBoletos = pers * 7
            if boletos > maxBoletos:
                print("Aún excedes el número de boletos permitidos.")
            else:
                self.calcularTotal(boletos, nombre)
        else:
            print("Opción no válida.")
    
    def calcularTotal(self, boletos, nombre):
        if boletos <= 2:
            cost = 12 * boletos
        elif boletos <= 5:
            cost = 12 * boletos * 0.90
        else:
            cost = 12 * boletos * 0.85
        
        print("Selecciona el método con el que deseas pagar: ")
        metPago = int(input("1. Tarjeta CINECO\n2. Efectivo\n"))
        if metPago == 1:
            cost *= 0.90
            print("Compra Guardada")
        elif metPago == 2:
            print("Compra Guardada")
        self.historial.append((nombre, cost)) 
        return cost
    
    def generarArchivoTexto(self):
        texto = self.generarTicket() 
        with open('archivo.txt', 'w') as archivo:
            archivo.write(texto)  
        print("Recibo generado: archivo.txt")
    
    def generarTicket(self):
        texto = "\nHistorial de ventas:\n"
        total_general = 0  
        for venta in self.historial:
            texto += "Comprador: {}, Total: ${:.2f}\n".format(venta[0], venta[1])
            total_general += venta[1]  
            
        texto += "\nTotal general de todas las ventas: ${:.2f}\n".format(total_general)
        return texto

def main():
    personas = Personas()
    while True:
        print("Puedes comprar únicamente 7 boletos por persona.")
        nombre = input("Introduce el nombre del comprador: ")
        pers = int(input("¿Cuántas personas vienen con él? "))
        maxBoletos = pers * 7
        boletos = int(input("¿Cuántos boletos deseas comprar? "))
        if boletos > maxBoletos:
            print("Has excedido el número máximo de boletos permitidos ({}).".format(maxBoletos))
            personas.excesoBoletos(pers, boletos, nombre)
        else:
            personas.calcularTotal(boletos, nombre)
        
        continuar = input("¿Deseas seguir comprando? (si/no): ").strip().lower()
        if continuar == "si":
            os.system("cls" if os.name == "nt" else "clear") 
        else:
            print("Disfrute su función.")
            print(personas.generarTicket()) 
            personas.generarArchivoTexto()  
            break

if __name__ == "__main__":
    main()

