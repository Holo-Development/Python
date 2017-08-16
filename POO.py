class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self, arranque):
        self.enmarcha=arranque
        if self.enmarcha:
            print("El coche esta encendido")
        else:
            print("El coche esta apagado")
        
    def estado(self):
        print(f"Ruedas: {self.ruedas}")
        print(f"Largo: {self.largoChasis}")
        print(f"Ancho: {self.anchoChasis}")


print("------Primer Objeto------")
miCoche=Coche()
print(f"El coche tiene {miCoche.largoChasis}")
miCoche.estado()
print(miCoche.arrancar(True))
print(miCoche.estado())
print("------Segundo objeto------")
segundoCoche=Coche()
segundoCoche.estado()
print(segundoCoche.arrancar(False))