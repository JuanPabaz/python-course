class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado exitosamente")
        else:
            print(f"El libro {self.title} ya ha sido prestado, no esta disponible")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"El libro {self.title} ha sido devuelto exitosamente.")
        else:
            print("El libro ya ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_books(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no se encuentra en la coleccion")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_books(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido añadido a la biblioteca")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado con exito")
    
    def show_available_books(self):
        print("Los libros disponibles son:")
        for book in self.books:
            if book.available:
                print(book.title)

book1 = Book("Satanas","Mario Mendoza")
book2 = Book("1984", "George Orwell")
user1 = User("Juan Pablo", 1)
library = Library()
library.add_books(book1)
library.add_books(book2)
library.register_user(user1)
library.show_available_books()
user1.borrow_books(book1)
user1.borrow_books(book1)
print(user1.borrowed_books)
