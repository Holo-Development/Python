tupla=("Rolando", 27,6,1989)
print(type(tupla))

lista=list(tupla)
print(type(lista))

nuevamente_tupla=tuple(lista)
print(type(nuevamente_tupla))

print("Rolando" in nuevamente_tupla)

print(nuevamente_tupla.count(1989))
print(len(nuevamente_tupla))

tupla_unitaria=("Una sola cosa",) #Tiene un solo elemento

nombre,dia,mes,ano=nuevamente_tupla #Asigna por el orden

print(nombre)