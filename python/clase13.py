numbers = [1,2,3,4,5,6]

for i in numbers:
    print(i)

for i in range(10):
    print(i)

fruits = ["Manzana","Mango","Fresa","Pera"]

for i in fruits:
    print("Fruta: ",i)

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1

numbers = [1,2,3,4,5,6]

for i in numbers:
    if i == 3:
        continue
    print(i)