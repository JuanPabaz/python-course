to_do = ["Dirigirnos al hotel",
         "Ir almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do[0])

numbers = [1,2,3,4,"cinco"]
print(numbers)
print(type(numbers))

mix = ["uno",2,3,4.5,True,[1,2,3]]
print(mix)
print(type(mix))

cadena = "Hola mundo"
print(cadena[0])
print(cadena[-1])

#print(mix[0:2])#Devuelve los elementos desde el 0 hasta el 2 sin incluir el 2
print(mix[:2])
print(mix[2:])#Devuelve todos los elementos desde 2 hasta el final

mix.append("hola soy append")#Le agrega al final un elemento a la lista
mix.append(["a","b"])
print(mix)

mix.insert(0,"Hola al inicio")#Agrega un elemento en la posicion deseada
print(mix)

print(mix.index("hola soy append"))#Devuelve la primera aparicion de un elemento en la lista

numbers = [1,2,100,90.45,3,4,5]
print(max(numbers))#Devuelve el elemento mayor de la lista
print(min(numbers))#Devuelve el elemento menor de la lista

del numbers[-1]#Elimina el elemento de la posicion dada
print(numbers)
del numbers[:2]#Elimina los elementos desde la posicion 0 hasta la 2
print(numbers)
#del numbers, elimina toda la lista