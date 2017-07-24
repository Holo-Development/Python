#Listas

primera_lista=["Poto","Caca","Pipi","Pepino"]

primera_lista.append("Dorato")

primera_lista.insert(0, "Papayita") #Agrega en la posicion deseada

primera_lista.extend(["Pepeyo","Tomaco","Tetino"]) #Agrega un nuevo listado
print(primera_lista.index("Tetino")) #Devuelve el indice de la posicion del elemento
print("Poto" in primera_lista) #busca si existe en el listado
print(primera_lista[:])
print(primera_lista[0:2]) #---> Porcion de la lista

primera_lista.remove("Caca") #--->Elimina elemento
primera_lista.pop() #Elimina el ultimo
print(primera_lista[:])

#El operador + hacelo mismo que extend y el * repite los elementos