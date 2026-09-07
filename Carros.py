from time import *
import os


class Car:
    def __init__(self, car_name, color, fuel):
        self.car_name = car_name
        self.color = color
        self.fuel = fuel
        self.car_components = {  #  Hay que ponerla dentro del constructor, si no sería una variable de la clase en lugar de variable de 
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
    def change_motor(self, new_piece):
        temporal_inventory.insert(0, self.car_components.pop('motor'))
        self.car_components.update({'motor': new_piece})
        temporal_inventory.remove(new_piece)


    def change_gearbox(self, new_piece):
        temporal_inventory.insert(0, self.car_components.pop('gearbox'))
        self.car_components.update({'gearbox': new_piece})
        temporal_inventory.remove(new_piece)


    def change_wheels(self, new_piece):
        temporal_inventory.insert(0, self.car_components.pop('wheels')) # estos parámetros estaban invertidos
        self.car_components.update({'wheels': new_piece})
        temporal_inventory.remove(new_piece)


    def change_chassis(self, new_piece):
        temporal_inventory.insert(0, self.car_components.pop('chassis')) # estos parámetros estaban invertidos
        self.car_components.update({'chassis': new_piece})
        temporal_inventory.remove(new_piece)


    def change_body(self, new_piece):
        temporal_inventory.insert(0, self.car_components.pop('body')) # estos parámetros estaban invertidos
        self.car_components.update({'body': new_piece})
        temporal_inventory.remove(new_piece)





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

carro1 = Car("Carro de Saul", "Amarillo", 100)

def interfaz_provisional():
    while True:
        os.system('cls')
        inventory_menu, car_components_menu = reload_menus()
        
        print(car_components_menu)
        menu = input(workshop_menu1)
        peace_index = int(input(inventory_menu))
        new_piece = temporal_inventory[peace_index-1]
        
        if   menu.upper() == "M"  : carro1.change_motor(new_piece)     
        elif menu.upper() == "CC" : carro1.change_gearbox(new_piece)
        elif menu.upper() == "R"  : carro1.change_wheels(new_piece)
        elif menu.upper() == "Ch" : carro1.change_chassis(new_piece)
        elif menu.upper() == "Crr": carro1.change_body(new_piece)


def reload_menus():
    
    inventory_menu = f"""
¿Cuál deseas instalar? (introduce el índice)
{get_inventory_as_column(temporal_inventory)}
> """

    car_components_menu = f"""
Estas son las piezas instaladas:
{get_car_components_as_column(carro1.car_components)}"""
    
    return inventory_menu,car_components_menu


def get_inventory_as_column(text):
    new_text = ""
    for i in range(len(text)):
        new_text += f"{i+1}. {text[i]} \n"
    return new_text


def get_car_components_as_column(text):
    new_text = ""
    for i in text.values():
        new_text += f" -{i} \n"
    return new_text



if __name__ == '__main__':
    interfaz_provisional()


#* Cucha pa acá Saul. Lo que hice fue extraer la lógica de la interfaz en una función provisional 
#* (de lo contrario, la función set_peace haría más de una cosa). 
#* Ahora tú debes programar esas 5 funciones. Cada una debe hacer lo siguiente: 
# 
#* 1. Quitar el tipo de pieza indicado del carro y ponerla en Temporal_inventory 
#* 2. Setear la pieza indicada


#! Métele :)


#Roger gracias por la ayuda, no se si lo que hice es como esperabas pero bueno, tengo un problema con la
#variable "new_piece" el compilador me dice que falta un argumento posicional en las funciones nuevas que hice


#*No hay de que bro, si algo puedo hacer sabiendo un poco más que tú es transmitirte ese poco de sabiduría :) 
#* PD: Creo que no es una buena práctica chatear por el código, pero como que estamos en familia dejemos esto así XD 