def greet(name, last_name="No tiene apellido"):
    print("Hola", name, last_name)

greet("Juan Pablo","Giraldo")
greet("Carolina")
greet(last_name="Giraldo",name="Cesar")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operacion")
        print("1 . Suma")
        print("2 . Resta")
        print("3 . Multiplicacion")
        print("4 . Division")
        print("5 . Salir")
        option = int(input("Ingresa la opcion: "))
        if option == 5:
            print("Saliendo de la calculadora")
            break    
        if option in [1,2,3,4]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == 1:
                print("la suma es:" ,add(num1,num2))
            elif option == 2:
                print("la resta es:" ,sub(num1,num2))
            elif option == 3:
                print("la multiplicacion es:" ,mul(num1,num2))
            elif option == 4:
                print("la division es:" ,div(num1,num2))
        else:
            print("Opcion no valida")
            break

calculator()

print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))