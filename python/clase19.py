class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age} años")

juan_pablo = Person("Juan Pablo",20)
carolina = Person("Carolina",19)

juan_pablo.greet()
carolina.greet()

class BankAcount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self,amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount} y su saldo es de {self.balance}")
        else:
            print("La cuenta esta inactiva y no se puede depositar")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount} y su saldo es de {self.balance}")
            else:
                print("No tiene saldo suficiente")
        else:
            print("La cuenta no esta activa")
        
    def deactivate_account(self):
        if self.is_active:
            self.is_active = False
            print("La cuenta ha sido desactivada")
        else:
            print("La cuenta ya esta inactiva")

    def activate_account(self):
        if self.is_active:
            print("La cuenta ya esta activa")
        else:
            self.is_active = True
            print("La cuenta ha sido activada")

account1 = BankAcount(juan_pablo.name,1000)
account2 = BankAcount(carolina.name,1000)

print(account1.account_holder)

account1.deposit(500)
print(account1.balance)
