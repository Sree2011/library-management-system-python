"""
Main Module

This module provides an interactive interface to the user

Modules:

    book: 
        functionalities to manage a library system, including book management, tracking the issue and return of books, and updating book statuses
    
    pandas:
        Python library for data visualisation
    
    numpy:
        Python library for data analysis


Functions:

    add_book(): 
        Adds a new book to the library.

    find_book(name): 
        Finds a book by its title.

    list_books(): 
        Retrieves a list of all books in the library.

    issue_book(name): 
        Issues a book and updates its status to "Yes".
        
    return_book(name): 
        Returns a book and updates its status to "No".


"""
import book
import pandas as pd
import numpy as np

# Generate documentation
import pydoc

def main():
    '''
    Params: none
    Returns: none

    Display welcome information to the user and
    do the operation based on the user's preference
    '''
    print("Hi! Welcome to our Library Management System!")
    name_user = input("What should we call you? ")
    print(f"Hello, {name_user}")
    print("If you want to add a book, press 1")
    print("If you want to see all books, press 2")
    print("If you want to get a book issued, press 3")
    print("If you want to return a book, press 4")

    # Ask for an option
    option_book = int(input())

    # Check for the functions
    if option_book == 1:
        add_book()
    elif option_book == 2:
        list_books()
    elif option_book == 3:
        issue_book()
    elif option_book == 4:
        return_book()
    else:
        print("Invalid option. Please try again.")


def add_book():
    '''
    Take the details of the book from the user as input
    and add them to the library file.

    Parameters:
        None
    Returns: 
        None

    '''

    # Get the details from the user
    print("Enter the details of the book you want to add:")
    name_book = input("Enter name: ").capitalize()
    author_book = input("Enter author: ").capitalize()
    volume_book = input("Enter volume number of the book (Eg. 1st): ")
    issued = "No"
    
    # Create a object of Book class from book.py to activate functions
    new_book = book.Book(name_book, author_book, volume_book, issued)

    # Call the add book function
    new_book.add_book()

# Get all the books present in the library
def list_books():

    '''
    Lists all the books available in the library.
    
    Params: none
    Returns: A pandas dataframe of the list of books in the library

    
    '''
    # Create a object of Book class from book.py to activate functions
    sample_book = book.Book("nn", "88", "4th", "Yes")

    # Specify the column headers to be printed
    columns = ["Name", "Author", "Volume", "Issued"]

    # Call the get all books function(return type is numpy array)
    books = sample_book.get_all_books()

    # Convert the result into a pandas dataframe for better readability
    list_books = pd.DataFrame(books, columns=columns)

    # Start the row index of the dataframe from 1
    list_books.index = np.arange(1, len(list_books) + 1)

    # print the dataframe
    print(list_books)

    # return the dataframe for further computations
    return list_books

def issue_book():

    '''
    Params: none
    Returns: none

    Takes the name of the book from the user as input
    and issue it to the user by updating issued status to 'yes'.
    '''

    # Get the list of all books and print
    df = list_books()

    # Ask user for the name of the book to be issued
    name = input("Enter the name of the book you want to be issued: ").capitalize()

    # Perform case-insensitive comparison with the dataframe
    result = df[df["Name"].str.lower() == name.lower()]
    
    # Check if result is empty
    if result.empty:
        print("No books found with that name.")
    # else issue the book and update the issued status
    else:
        print("Books found:")
        print(result)
        # Assuming issue_book method updates the book's issued status

        # Extract the columns from the dataframe by index and create an object of Book class
        sample_book = book.Book(result.iloc[0]["Name"], result.iloc[0]["Author"], result.iloc[0]["Volume"], result.iloc[0]["Issued"])
        
        # Call the issue book function
        sample_book.issue_book(name)

def return_book():

    '''
    Params: none
    Returns: none

    Takes the name of the book from the user as input
    and returns it to the library by updating issued status to 'no'.
    '''
    df = list_books()
    name = input("Enter the name of the book you want to return: ").capitalize()
    result = df[df["Name"].str.lower() == name.lower()]
    
    if result.empty:
        print("No books found with that name.")
    else:
        print("Books found:")
        print(result)
        # Assuming issue_book method updates the book's issued status
        sample_book = book.Book(result.iloc[0]["Name"], result.iloc[0]["Author"], result.iloc[0]["Volume"], result.iloc[0]["Issued"])
        sample_book.return_book(name)


if __name__ == "__main__":
    main()

