from random import *
components_car = {  #  Hay que ponerla dentro del constructor, si no sería una variable de la clase en lugar de variable de 
            'motor': "MotorX",   # instacia y todas las instancias de carro tendrían los mismos componentes 
            'gearbox': "CajaCambA",
            'wheels': "RuedasA",
            'chassis': "ChasisA",
            'body': "CrrA"
        }
#Aqui testeamos nuestros codigos
def change_motor(new_peace): #Cambiar motor

    print("Cambiando pieza vieja...")
    temporal_inventory.insert(0, components_car.pop('motor'))#El error que corregi fue en el index que lo puse mal
    components_car.update({'motor': new_peace})
    temporal_inventory.remove(new_peace)
#Roger aqui puse un loop para que vieras la lista del inventario temp, si quieres la quitas
    for piece in temporal_inventory:
        print(piece)
    print(components_car)
       

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
        
        if   menu.upper() == "M"  : change_motor(new_peace)     #funciones a programar
        elif menu.upper() == "CC" : change_gearbox(new_peace)
        elif menu.upper() == "R"  : change_wheels(new_peace)
        elif menu.upper() == "Ch" : change_chassis(new_peace)
        elif menu.upper() == "Crr": change_body(new_peace)


print(interfaz_provisional())