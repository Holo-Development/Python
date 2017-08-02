# pylint: enable-msg=C0103
# pylint: disable=C0103
es_verdadero=True
es_falso=False

def evaluacion(argumento):
    """Evalua el argumento y retorna true o false"""
    if argumento in ("verdadero","Verdadero","VERDADERO"):
        return es_verdadero
    #elif algo<algo2<algo3:
        pass
    else:
        return es_falso  


args = input()
numero = input()
print(type(int(numero)))
print(evaluacion(args))

def eleccion_asignaturas():
    """Permite elegir asignaturas"""
    print("Asignaturas Optativas")
    print("Eleccion de asignaturas")
    print("1) Arduino".upper())
    print("2) Python".upper())
    print("3) Java".upper())

    asignaturas = {1:"Arduino", 2:"Python", 3:"Java"}
    opcion = int(input("Asignatura a elegir: ".upper()))

    if opcion in asignaturas:
        print("La asignatura elegida es: "+asignaturas[opcion])
    else:
        print("Eleccion erronea")

eleccion_asignaturas()