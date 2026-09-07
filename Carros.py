
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
#Roge aqui dividi el codigo en funciones simples, las que me dijiste 
    def change_motor(self, new_peace): #Cambiar motor

        print("Cambiando pieza vieja...")
        temporal_inventory.insert(0, f"{self.components_car.pop('motor')}")
        self.components_car.update({'motor': new_peace})
        temporal_inventory.remove(new_peace)
#Roger aqui puse un loop para que vieras la lista del inventario temp, si quieres la quitas
        for piece in temporal_inventory:
            print(piece)
       
                
            
    def change_gearbox(self, new_peace):
            print("Cambiando pieza vieja...")
            temporal_inventory.insert(2, self.components_car.pop('gearbox'))
            self.components_car.update({'gearbox': new_peace})
            temporal_inventory.remove(new_peace)
            

    def change_wheels(self, new_peace):
        print("Cambiando pieza vieja...")
        temporal_inventory.insert(self.components_car.pop('wheels'), -1)
        self.components_car.update({'wheels': new_peace})
        temporal_inventory.remove(new_peace)
        for key, value in self.components_car.items():
            print(f"{key}: {value}")
            print(temporal_inventory)
                
            
    def change_chassis(self, new_peace):
                print("Cambiando pieza vieja...")
                temporal_inventory.insert(self.components_car.pop('chassis'), -1)
                self.components_car.update({'chassis': new_peace})
                temporal_inventory.remove(new_peace)
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(temporal_inventory)
            
            
    def change_body(self, new_peace):
                print("Cambiando pieza vieja...")
                temporal_inventory.insert(self.components_car.pop('body'), -1)
                self.components_car.update({'body': new_peace})
                temporal_inventory.remove(new_peace)
                for key, value in Carro.components_car.items():
                    print(f"{key}: {value}")
                print(temporal_inventory)
                    
             



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



if __name__ == '__main__':
    print(interfaz_provisional())


#* Cucha pa acá Saul. Lo que hice fue extraer la lógica de la interfaz en una función provisional 
#* (de lo contrario, la función set_peace haría más de una cosa). 
#* Ahora tú debes programar esas 5 funciones. Cada una debe hacer lo siguiente: 
# 
#* 1. Quitar el tipo de pieza indicado del carro y ponerla en Temporal_inventory 
#* 2. Setear la pieza indicada


#! Métele :)


#Roger gracias por la ayuda, no se si lo que hice es como esperabas pero bueno, tengo un problema con la
#variable "new_peace" el compilador me dice que falta un argumento posicional en las funciones nuevas que hice