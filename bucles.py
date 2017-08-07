import math

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    """Ciclo for"""
    print("Holo "+i)

for i in ["Pildoras","Informaticas","Python"]:
    print("Hola", end=" ")

for i in range(10):
    print(f"Valor de la variable {i}")

for i in range(0,10,2):
    """For desde hasta con el avance del for"""
    print(i)

print(len("Rolando"))


i=1

while i<=10:
    print(f"Ejecucion {str(i)}")
    i=i+1
print("Termino la ejecucion")


edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
    print("Has ingresado una edad incorrecta, vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print(f"Edad del aspirante es {str(edad)}")



print("Raiz cuadrada")
numero=int(input("Introduce un numero positivo por favor: "))

intentos=0

while numero<0:
    print("No existe una raiz negativa")

    if intentos==2:
        print("Intentos finalizados")
        break
    numero=int(input("Introduce un numero positivo por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print(f"Raiz cuadrada: {solucion} de {numero}")


for letra in "Python":
    if letra=="h":
        continue
    print(f"Viendo la letra:{letra}")

variable="Pildoras Informaticas"
contador=0
for letra in variable:
    if letra == " ":
        continue

    contador+=1
else:
    print("No se cumple la el ciclo")

    
print(f"La cantidad de letras es: {contador}")