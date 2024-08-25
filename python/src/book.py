import bookutils

class Book:
    def __init__(self, name, author, volume, issued):
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

    def find_book(self, name):
        result = bookutils.find_book("./python/data/books.csv", name)
        return result

    def get_all_books(self):
        return bookutils.get_books("./python/data/books.csv")

    def issue_book(self, name):
        result = self.find_book(name)
        if result.empty:
            print("No books found with that name.")
        else:
            bookutils.update_book_status("./python/data/books.csv", name, "Yes")
            print("Book issued: ")
            result = self.find_book(name)
            print(result)

    def return_book(self, name):
        bookutils.update_book_status("./python/data/books.csv", name, "No")
