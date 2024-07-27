# .count() Cuenta el numero de aparaciones de un caracter en la cadena
# .capitalize()
# .title() 
# .swapcase() 
# .replace(,) Reemplaza todas las apariciones de un caracter en la cadena por otro caracter
# .split() 
# .strip() Elimina los espacios en blanco al principio y final de la cadena
# .lstrip() 
# .rstrip() 
# .find() Busca la primera aparicion de un caracter en la cadena y devuelve su indice
# .index() 
# eval()	#Este y el siguiente son super métodos
# exec()

#String con comillas dobles
name = "Juan Pablo"
caracter = "c"

#String con comillas simples
name = 'Juan Pablo'

#String con comillas triples
name = '''Juan Pablo
Giraldo'''#Esto sirve para mostrar los saltos de linea

print(name)

print(type(name)) #type(variable) nos da el tipo de variable

#Posiciones
name2 = 'Juan Pablo Giraldo'
print(name2[0])#Esto devuelve el caracter en la posicion 0, que es la inicial.
print(name2[-1])#Esto devuelve el ultimo caracter de la cadena.

#Concatenar Strings
name3 = "Juan Pablo"
lastname = "Giraldo"
print(name3 + " " + lastname)

#Replicas
print((name3 + " ")*3)

#Tamaño
print(len(lastname))#Devuelve el tamaño de la cadena

#Metodos de la clase String
print(name.lower())#Lleva toda la cadena a minuscula
print(name.upper())#Lleva todo la cadena a mayuscula
print(name.strip())#Quita los espacios en blanco al principio y al final de la cadena

