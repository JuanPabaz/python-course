#Ejemplo iterador
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

for i in my_list:
    print(i)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)