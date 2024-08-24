from utils import *

class Book:
    def __init__(self,name,author,volume,issued):
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued

    def add_book(self):
        book_array = self.__dict__
        append_dict_to_csv("./python/data/books.csv", book_array)
        print("Book Added:")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Volume: {self.volume}")
        print(f"Issued: {self.issued}")


Book1 = Book("lisa","petekr",2,False)
Book1.add_book()