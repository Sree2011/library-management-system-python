import bookutils

'''
Implement a book class to perform operations on the books.
'''
class Book:

    def __init__(self, name, author, volume, issued):
        """
    Creates the object of book class

    Parameters
    ----------

    name : str
        The title of the book.
    author : str
        The author of the book.
    volume : str
        The volume number of the book.
    issued : str
        Issued status of the book.

    Returns
    -------
    Book
        An object of the book class.
    
    """
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued

    def add_book(self):
        """
        Add a new book to the library.

        Parameters
        ----------
        name : str
            The title of the book.
        

        Returns
        -------
        bool
            True if the book was added successfully, False otherwise.
        
        
    """
        book_array = self.__dict__
        bookutils.append_dict_to_csv("./python/data/books.csv", book_array)
        print("Book Added:")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Volume: {self.volume}")
        print(f"Issued: {self.issued}")

    def find_book(self, name):
        '''
        Finds the book by name from the library

        Parameters
        ----------

        name : str
            The title of the book

        Returns
        -------
        result : A pandas DataFrame 
            A dataframe containing all fields of the book found

        '''

        result = bookutils.find_book("./python/data/books.csv", name)
        return result

    def get_all_books(self):
        '''
        Gets the list of all books from the library

        Parameters
        ----------
        None

        Returns
        -------
        result : A pandas DataFrame
            A dataframe containing all fields of all the books in the library

        '''
        return bookutils.get_books("./python/data/books.csv")

    def issue_book(self, name):
        '''
        Issues the book and updates the "issued" column to "Yes"

        Parameters
        ----------

        name : str
            The title of the book

        Returns
        -------
        None

        '''
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