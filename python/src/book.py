"""
Book Module

This module provides functionalities to manage a library system, including book management, tracking the issue and return of books, and updating book statuses.
Modules:

    bookutils: 
        Utility functions for handling book data operations such as appending to CSV, finding books, and updating book status.

Classes:

    Book: 
        Represents a book in the library and provides methods to add, find, issue, and return books.

Functions:

    add_book(): 
        Adds a new book to the library.

    find_book(name): 
        Finds a book by its title.

    get_all_books(): 
        Retrieves a list of all books in the library.

    issue_book(name): 
        Issues a book and updates its status to "Yes".
        
    return_book(name): 
        Returns a book and updates its status to "No".

"""
import bookutils




class Book:

    def __init__(self, name, author, volume, issued):
        
        """
        Creates the object of the Book class.

        Parameters:
            name (str): The title of the book.
            author (str): The author of the book.
            volume (str): The volume number of the book.
            issued (str): Issued status of the book.

        Returns:
            Book: An object of the Book class.
        
        """
        
        self.name = name
        self.author = author
        self.volume = volume
        self.issued = issued

    def add_book(self):
        """
       Adds the book into the library

       This method takes the book's attributes and appends them to a CSV file, 
       effectively adding the book to the library's records.

        Parameters:
            None

        Returns:
            None     
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

        Parameters:
            name (str): The title of the book to be found
        
        Returns:
            result (pandas.DataFrame): A pandas dataframe containing the details of the book

        '''

        result = bookutils.find_book("./python/data/books.csv", name)
        return result

    def get_all_books(self):
        '''
        Gets the list of all books from the library

        Parameters:
            none

        Returns:
            result (pandas.DataFrame): A pandas DataFrame containing the details of all books
        '''
        result = bookutils.get_books("./python/data/books.csv")
        return result

    def issue_book(self, book_name,member_name):
        '''
        Issues the book and updates the "issued" column to "Yes"

        Parameters:
            None
        
        Returns:
            None
        
        '''
        result = self.find_book(book_name)
        if result.empty:
            print("No books found with that name.")
        else:
            bookutils.update_book_status("./python/data/books.csv", book_name, "Yes")
            book = self.find_book(book_name)
            print(f"Book issued: {book}")

    def return_book(self, name):
        '''
        Returns the book and updates the "issued" column to "No"

        Parameters:
            None
        
        Returns:
            None
        
        '''
        bookutils.update_book_status("./python/data/books.csv", name, "No")
        print("Book returned:")
        result = self.find_book(name)
        print(result)