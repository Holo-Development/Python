es_verdadero=True
es_falso=False

def evaluacion(argumento):
    if argumento == "verdadero" or argumento == "Verdadero":
        return es_verdadero
    else:
        return es_falso  


argumento = input()
numero=input()
print(type(int(numero)))
print(evaluacion(argumento))