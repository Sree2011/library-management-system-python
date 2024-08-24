# Add a Book: Enter the book details (ID, title, author) to add a new book to the library.

class Book:
    def __init__(self,name,author,volume,issued):
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued
    def print_book(self):
        print(self.__dict__)


Book1 = Book("hapot","peter",2,False)
Book1.print_book()