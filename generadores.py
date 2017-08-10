def generadorPares(limite):
    """funcion que genera pares con un listado"""
    num=1
    listado=[]

    while num<limite:
        listado.append(num*2)

        num+=1
    return listado


print(generadorPares(20))

def generaPares(limite):
    """Metodo que usa un generador, que devuelve un iterable"""
    num=1

    while num<limite:

        yield num*2

        num+=1

devuelvePares=generaPares(10)



print(next(devuelvePares))
print("Algo de codigo")
print(next(devuelvePares))
print("Algo mas")
print(next(devuelvePares))

for i in devuelvePares:
    print(i)

def devuelve_ciudades(*ciudades):
    """Accede a los elementos de los elementos sin necesidad de un for anidado"""
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas=devuelve_ciudades("Santiago", "Okinawa", "Madrid", "Berlin")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))