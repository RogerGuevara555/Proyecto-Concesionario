
from Llantas import *
from Base_data import *
class Carros:

        def __init__(self, name, clase, model, price, type):
            self.name = name
            self.clase = clase
            self.model = model
            self.price = price
            self.type = type
            
            
        
        
        
    
def agregar():
        input("Selecciona entre (LLantas, Motores, Pintura, Transmisores, Caja de cambio, etc):")
    
        if input("Selecciona entre (LLantas, Motores, Pintura, Transmisores, Caja de cambio, etc):") == "M":
            pass
        elif input("Selecciona entre (LLantas, Motores, Pintura, Transmisores, Caja de cambio, etc):") == "LL":
            print(main_1())
        elif input("Selecciona entre (LLantas, Motores, Pintura, Transmisores, Caja de cambio, etc):") == "R":
            print("A agregado un motor remolque a su carrito")
        else:
            input("Select a piece: ")        



def main():
        cars = input("Put the name of your car: ")
        print((f"You car is a {cars}"))
        input("Deseas adquirir alguna pieza de carro (Y/N): ")
    

    
        while True:
            if input("Deseas adquirir algunq pieza de carro (Y/N): ") == "Y":
                print(agregar())
            elif not input("Deseas adquirir algunq pieza de carro (Y/N): ") == "Y":
                print("Respuesta invalida")
                input("Deseas adquirir algunq pieza de carro (Y/N): ")


if __name__ == "__main__":
    print (main())