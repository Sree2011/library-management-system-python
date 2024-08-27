import bookutils

'''
Implement a book class to perform operations on the books.
'''
class Book:

    '''
    The constructor of Book class with parameters
    Params: Book details (name, author,volume number, issued status)
    Returns: Creates an object of the class when called with class name
    '''
    def __init__(self, name, author, volume, issued):
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued

    def add_book(self):
        """
        Add a new book to the library.

        Parameters
        ----------
        book_id : int
            The unique identifier for the book.
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The year the book was published.

        Returns
        -------
        bool
            True if the book was added successfully, False otherwise.
        
        Raises
        ------
        ValueError
            If the book_id already exists in the library.
    """
        book_array = self.__dict__
        bookutils.append_dict_to_csv("./python/data/books.csv", book_array)
        print("Book Added:")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Volume: {self.volume}")
        print(f"Issued: {self.issued}")

    '''
    Finds the book by name

    Params: name of the book to find

    '''
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
        print("Book returned:")
        result = self.find_book(name)
        print(result)