def adicion(num1,num2):
    return num1+num2

def sustraccion(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion erronea"
while True:
    try:
        operacion=input("Introduce la operacion(adicion,sustraccion,multiplicacion,division)")
        opcion1=int(input("Introduce el primer numero: "))
        opcion2=int(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("Introduce un numero por favor")

    except:
        print("Esta es una excepcion general")

while operacion is not ("salir","Salir","SALIR"):
    if operacion in ("adicion", "Adicion", "ADICION"):
        print(adicion(opcion1,opcion2))
    elif operacion in ("sustraccion", "Sustraccion", "SUSTRACCION"):
        print(sustraccion(opcion1,opcion2))
    elif operacion in ("multiplicacion", "Multiplicacion", "MULTIPLICACION"):
        print(multiplicacion(opcion1,opcion2))
    elif operacion in ("division","Division", "DIVISION"):
        print(division(opcion1,opcion2))
    elif operacion in ("salir", "Salir", "SALIR"):
        break
    else:
        try:
            operacion=input("Introduce la operacion(adicion,sustraccion,multiplicacion,division)")
            opcion1=int(input("Introduce el primer numero: "))
            opcion2=int(input("Introduce el segundo numero: "))
            
        except ValueError:
            print("Introduce un numero por favor")

    try:
        operacion=input("Introduce la operacion(adicion,sustraccion,multiplicacion,division)")
        opcion1=int(input("Introduce el primer numero: "))
        opcion2=int(input("Introduce el segundo numero: "))
        
    except ValueError:
        print("Introduce un numero por favor")
    finally:
        print("El programa termino")

    
    #Crear una excepcion propia

    def evaluaEdad(edad):

        if edad<0:
            raise TypeError("Este es un mensaje personalizado de error")

        if edad < 20:
            return "Eres muy joven"
        elif edad < 40:
            return "Eres joven"
        elif edad < 65:
            return "Eres maduro"
        elif edad < 100:
            return "Cuidate..."

try:
    print(evaluaEdad(18))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)