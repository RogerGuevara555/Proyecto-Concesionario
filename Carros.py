#from Piezas import *
from time import *



class Carro:
    def __init__(self, name_car, color, fuel):
        self.name_car = name_car
        self.color = color
        self.fuel = fuel
        self.components_car = {  #  Hay que ponerla dentro del constructor, si no sería una variable de la clase en lugar de variable de 
            'motor': "MotorX",   # instacia y todas las instancias de carro tendrían los mismos componentes 
            'gearbox': "CajaCambA",
            'wheels': "RuedasA",
            'chassis': "ChasisA",
            'body': "CrrA"
        }
        
#Metodo para arrancar el carro    
    def start(components):
        pass

    def run():
        pass
#Metodo para agegar piezas(Roger cuando hagas lo de las pieza me avisas para empezar a trabajar en lo ue falta)
#Pp hay que refactorizar todo esto primero.         pd: Roger
    def set_component():
                
        
        while True:
            menu = input("Seleccione la pieza a cambiar (M,CC,R,Ch,Crr): ")
            
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
#Carro.set_component()              



# Esto lo dejo afuera, ya que el inventario no le pertenece al carro, sino al dueño. 
# Por ende, iría en una clase User que Justin está implementando, creo.
temporal_inventory = ["MotorA", "MotorB", "MotorC", "CajaCambB", "CajaCambC", "RuedasB", 'ChasisA']
workshop_menu1 ="""

Seleccione la pieza a cambiar 
[===========================]
| (M)   -> Motor            |
| (CC)  -> Caja de cambios  |
| (R)   -> Ruedas           |
| (Ch)  -> Chasis           |
| (Crr) -> Carrocería       |
[===========================]

> """

def get_list_text(text):
    new_text = ""
    for i in range(len(text)):
        new_text += f"{i+1}. {text[i]} \n"
    return new_text

workshop_menu2 = f"""
¿Cuál deseas instalar? (introduce el índice)
{get_list_text(temporal_inventory)}
> """



def interfaz_provisional():
    while True:
        menu = input(workshop_menu1)
        peace_index = int(input(workshop_menu2))
        new_peace = temporal_inventory[peace_index-1]
        
        if   menu.upper() == "M"  : Carro.change_motor(new_peace)     #funciones a programar
        elif menu.upper() == "CC" : Carro.change_gearbox(new_peace)
        elif menu.upper() == "R"  : Carro.change_wheels(new_peace)
        elif menu.upper() == "Ch" : Carro.change_chassis(new_peace)
        elif menu.upper() == "Crr": Carro.change_body(new_peace)


if __name__ == "__main__":
    interfaz_provisional()


#* Cucha pa acá Saul. Lo que hice fue extraer la lógica de la interfaz en una función provisional 
#* (de lo contrario, la función set_peace haría más de una cosa). 
#* Ahora tú debes programar esas 5 funciones. Cada una debe hacer lo siguiente: 
# 
#* 1. Quitar el tipo de pieza indicado del carro y ponerla en Temporal_inventory 
#* 2. Setear la pieza indicada


#! Métele :)
