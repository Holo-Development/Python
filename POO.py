class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self, arranque):
        self.__enmarcha=arranque
        if self.__enmarcha:
            print("El coche esta encendido")
        else:
            print("El coche esta apagado")
        
    def estado(self):
        print(f"Ruedas: {self.__ruedas}")
        print(f"Largo: {self.__largoChasis}")
        print(f"Ancho: {self.__anchoChasis}")


print("------Primer Objeto------")
miCoche=Coche()
print(f"El coche tiene {miCoche.__largoChasis}")
miCoche.estado()
print(miCoche.arrancar(True))
print(miCoche.estado())
print("------Segundo objeto------")
segundoCoche=Coche()
segundoCoche.estado()
print(segundoCoche.arrancar(False))