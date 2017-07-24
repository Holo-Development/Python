diccionario_paises_capitales={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres", "Chile":"Santiago"}
print(diccionario_paises_capitales)
diccionario_paises_capitales["Italia"]="Lisboa"
print(diccionario_paises_capitales)
diccionario_paises_capitales["Italia"]="Roma"
print(diccionario_paises_capitales)
print(diccionario_paises_capitales["Chile"])

del diccionario_paises_capitales["Francia"]
print(diccionario_paises_capitales)

######################################################

tupla=["Chile", "Canada", "Reino Unido", "Alemania"]

mi_diccionario={tupla[0]:"Santiago", tupla[1]:"Vancouver", tupla[2]:"Londres", tupla[3]:"Berlin"}
print(mi_diccionario["Canada"])

midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario["anillos"])
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))