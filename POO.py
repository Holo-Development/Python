class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True
        
    def estado(self):
        if self.enmarcha:
            print("El coche esta encendido")
        else:
            print("El coche esta apagado")



miCoche=Coche()

print(f"El coche tiene {miCoche.largoChasis}")
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())