class Vehiculos():
	def __init__(self, marca, modelo):
		self.__marca=marca
		self.__modelo=modelo
		self.__encendido=False
		self.__acelerado=False
		self.__frenado=False

	def encender(self):
		self.__encendido=True

	def frenar(self):
		self.__frenado=True

	def estado(self):
		print("Marca: ", self.__marca)
		print("Modelo: ", self.__modelo)
		print("Encendido: ", self.__encendido)
		print("Acelerado: ", self.__acelerado)
		print("Frenado: ", self.__frenado)

class Moto(Vehiculos):
	__andarEnUnaRueda=""

	def andarUnaRueda(self):
		self.__andarEnUnaRueda="Andando en una rueda"

	def estado(self):
		super().estado()

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.__cargado=cargar

		if self.__cargado:
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

class ATV(Moto):
	pass

class Electricos():
	def __init__(self):
		self.__autonomia=100

	def cargaEnergia(self):
		self.__cargando=True

class BicicletaElectrica(Vehiculos, Electricos):
		def __init__(self, bateria, marca, modelo):
			super().__init__(marca, modelo)
			self.__bateria=100

		def cargaEnergia(self):
			super().cargaEnergia()


miMoto=Moto("Honda", "CBR")
print(miMoto.andarUnaRueda())
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.encender()
miFurgoneta.estado()
miFurgoneta.carga(True)

print(isinstance(miMoto, Vehiculos))
