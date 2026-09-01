from abc import ABC, abstractmethod

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


class Peace ():
    
    def __init__(self, brand:str, qualty:chr, condition:chr, size:chr, price:int):
        self.brand = brand              # Toyota
        self.qualty = qualty            # - = + # & 
        self.condition = condition      # N U R
        self.size = size                # b m s
        self.price = price              # 500$
    
    @abstractmethod
    def __str__(self):
        return f"{self.condition}{self.size} {self.qualty}Pieza{self.brand}{self.qualty}"
    
    @abstractmethod
    def get_sound(self):
        return None


class Motor (Peace):
    
    def __init__(self, brand, qualty, condition, size, price, fuel=0):
        super().__init__(brand, qualty, condition, size, price)
        self.fuel = fuel
    
    
    def __str__(self):
        return f"{self.condition}{self.size} {self.qualty}Motor{self.brand}{self.qualty}"
    
    def fill_fuel(self, cuantity:int):
        self.fuel += cuantity
    
    def use_fuel(self, cuantity:int):
        self.fuel -= cuantity
    
    def get_sound(self):
        return "Brrrr"
    
    

if __name__ == "__main__":
    motor = Peace("Toyota", '=', 'N', 'm', 500)
    print(motor)


