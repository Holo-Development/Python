class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self, arranque):
        self.__enmarcha=arranque

        if self.__enmarcha:
            chequeo=self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return "El coche esta encendido"
        elif self.__enmarcha and chequeo==False:
            return "Hay problemas"
        else:
            return "El coche esta apagado"
        
    def estado(self):
        print(f"Ruedas: {self.__ruedas}")
        print(f"Largo: {self.__largoChasis}")
        print(f"Ancho: {self.__anchoChasis}")

    def __chequeo_interno(self): #Metodo encapsulado
        print("Realizando chequeo interno")

        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"

        if self.gasolina=="Ok" and self.aceite=="Ok":
            return True
        else:
            return False


print("------Primer Objeto------")
miCoche=Coche()
#print(f"El coche tiene {miCoche.__largoChasis}")
miCoche.estado()
print(miCoche.arrancar(True))
print(miCoche.estado())
print("------Segundo objeto------")
segundoCoche=Coche()
segundoCoche.estado()
print(segundoCoche.arrancar(True))