
#?   CALIDADES:
#* (-) Pieza obsoleta (1pto)
#* (=) Pieza común en carros normales (2ptos)
#* (+) Pieza fabricada para carreras (3ptos)
#* (#) Pieza usada solo por el ejército (4ptos)
#* (&) Milagro de la ingeniería automovilística (5ptos)

#?   Estados
#* (N) Pieza nueva
#* (U) Pieza usada
#* (R) Pieza rota

#?   Tamaños
#* (b) Grande
#* (m) Mediano
#* (s) pequeño


#?   Representación de una pieza:
#* print(pieza)
#* >> Nm =MotorToyota=


from abc import ABC, abstractmethod


class Peace (ABC):

    def __init__(self, brand:str, qualty:chr, condition:chr, size:chr, price:int):
        self.brand = brand              # Toyota
        self.qualty = qualty            # - = + # & 
        self.condition = condition      # N U R
        self.size = size                # b m s
        self.price = price              # 500$

    def __str__(self):
        peace_type = self.__class__.__name__
        pc_qual = self.qualty
        pc_cond = self.condition
        pc_size = self.size
        pc_brand = self.brand
        return f"({pc_cond}|{pc_size}) {pc_qual}{peace_type}{pc_brand}{pc_qual}"

    @abstractmethod
    def get_sound(self):
        return None



class Motor (Peace):

    def __init__(self, brand, qualty, condition, size, price, fuel=0):
        super().__init__(brand, qualty, condition, size, price)
        self.fuel = fuel


    def fill_fuel(self, cuantity:int):
        self.fuel += cuantity

    def use_fuel(self, cuantity:int):
        self.fuel -= cuantity

    def get_sound(self) -> str:
        return "Swanfanson"



class Wheels (Peace):

    def __init__(self, brand, qualty, condition, size, price):
        super().__init__(brand, qualty, condition, size, price)

    def get_sound(self) -> str:
        return super().__str__()



class Chassis (Peace):

    def __init__(self, brand, qualty, condition, size, price):
        super().__init__(brand, qualty, condition, size, price)

    def get_sound(self) -> str:
        return super().__str__()



class Body (Peace):

    def __init__(self, brand, qualty, condition, size, price, color):
        super().__init__(brand, qualty, condition, size, price)
        self.color = color

    def get_sound(self) -> str:
        return super().__str__()



class Gearbox (Peace):

    def __init__(self, brand, qualty, condition, size, price):
        super().__init__(brand, qualty, condition, size, price)

    def get_sound(self) -> str:
        return super().__str__()




if __name__ == "__main__":
    motor = Wheels("Toyota", '=', 'N', 'm', 500)
    print(motor)


