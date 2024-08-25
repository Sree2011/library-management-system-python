import bookutils
import member
class Book:
    def __init__(self,name,author,volume,issued):
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued

    def add_book(self):
        book_array = self.__dict__
        bookutils.append_dict_to_csv("./python/data/books.csv", book_array)
        print("Book Added:")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Volume: {self.volume}")
        print(f"Issued: {self.issued}")

    def get_all_books(self,name):
        return bookutils.get_books()

    def issue_book(self,name):
        bookutils.issue_book()
        print(f"{name} book issued")

Book1 = Book("asha","peter",1,False)
# Book1.add_book()
name = "Clean Code"
Book1.issue_book(name)