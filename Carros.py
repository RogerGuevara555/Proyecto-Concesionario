from Piezas import *
from time import *

class Carro:
    components_car = {'motor': "MotorX", 
                      'cajacamb': "CajaCambA",
                      'ruedas': "RuedasA",
                      'chasis': "ChasisA",
                      'carroceria': "CrrA"}
    temp_inventory = ["MotorA", "MotorB", "MotorC", "CajaCambB", "CajaCambC", "RuedasB", 'ChasisA']
    def __init__(self, name_car, color, fuel):
        self.name_car = name_car
        self.color = color
        self.fuel = fuel
        
#Metodo para arrancar el carro    
    def start(components):
        pass

    def run():
        pass
#Metodo para agegar piezas(Roger cuando hagas lo de las pieza me avisas para empezar a trabajar en lo ue falta)
    def set_component():
                
        
        while True:
            menu = (input("Seleccione la pieza a cambiar (M,CC,R,Ch,Crr): "))
            
            if menu.upper() == "MA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
#Roger aqui puse un loop para que vieras la lista del inventario temp, si quieres la quitas
                for piece in Carro.temp_inventory:
                    print(piece)
                print(Carro.temp_inventory)
            elif menu.upper() == "MB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(2, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(Carro.temp_inventory)
            elif menu.upper() == "MC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(3, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[2]})
                Carro.temp_inventory.remove(Carro.temp_inventory[2])
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(Carro.temp_inventory)
            elif menu.upper() == "RA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(4, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[3]})
                Carro.temp_inventory.remove(Carro.temp_inventory[3])
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(Carro.temp_inventory)
            elif menu.upper() == "RB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(Carro.temp_inventory)
            elif menu.upper() == "RC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(Carro.temp_inventory)
            elif menu.upper() == "CAJACAMBA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(1, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])    
            elif menu.upper() == "CAJACAMBB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CAJACAMBC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CHA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CHB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CHC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CRRA":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CRRB":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == "CRRC":
                print("Cambiando pieza vieja...")
                Carro.temp_inventory.insert(0, Carro.components_car.pop('motor'))
                Carro.components_car.update({'motor': Carro.temp_inventory[1]})
                Carro.temp_inventory.remove(Carro.temp_inventory[1])
            elif menu.upper() == menu.isdigit():
                break
            else:
                break
print(Carro.set_component())              

