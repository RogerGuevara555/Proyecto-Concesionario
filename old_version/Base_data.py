class Carro:
        
    
    
    def __init__(self, name, modelo, precio):
        self.name = name
        self.modelo = modelo
        self.precio = precio
        
    def add():
        print("*********Menu de Piezas********** ")

        lista = {1 :'Motores', 
                 2 :'Llantas', 
                 3 :'Carroceria', 
                 4 :'Transmisores',
                 5 :'Aerodinamica', 
                 6 :'Interiores',
                 7 :'Ventanillas', 
                 8 :'Trubo', 
                 9 :'Escape'}
        
        def LLantas():
            llanta = {1 :'dergdd3, Toyota, $350',
                      2 :'rgioukkk67h, Mercedez-Benz, 400', 
                      3 :'gttgbvcedrhfj, Cadilac, $550',
                      4 :'ssvovnds24ttekk, Honda, $600'}
            
        for key, value in lista.items():
            print(key, value)
        
        select = int(input('Select e piece (1,2,3,4,5....): '))
        
        if select == 1:
            print(Carro.add())

def main():

    print('Bienvenido al Taller Juarez')
    enter = input("Desea entrar al la seccion de tuneo (Y/N): ").upper()
    
    if not enter == "Y":
        print("Invalida respuesta")
    elif enter == 'N':
        print("Gracias por su visita")
    else:
        print(Carro.add())

                
if __name__ == '__main__':
    print(main())