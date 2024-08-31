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

    option_non_members():
        Presents options for non-members to add a book or view all books.

    option_members():
        Presents options for members to add a book, view all books, issue a book, or return a book.

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
from datetime import datetime
import book
import member
import pandas as pd
import numpy as np

# Generate documentation
import pydoc

def main():
    '''
    Display welcome information to the user and
    do the operation based on the user's preference

    Parameters:
        None
    Returns:
        None
    '''
    print("Hi! Welcome to our Library Management System!")
    name_user = input("What should we call you? ")
    print(f"Hello, {name_user}")

    obj1 = member.Member("ll", "sak@gmail.com", datetime.now(), "Free")
    mem = obj1.find_member(name_user)

    if not mem.empty:
        print("You are not a member of our library. Would you like to be one? It's Free..Kindly type yes or no")
        op = input().lower()
        if op == "yes":
            add_member()
            option_members()
        elif op == "no":
            print("You can't get a book issued if you are not a member. Are you sure?")
            op = input().lower()
            if op == "yes":
                add_member()
                option_members()
            elif op == "no":
                print("No worries, thank you.")
                print("If you want to get a book issued, become a member")
                option_non_members()
    else:
        option_members()

def option_non_members():
    """
    Presents options for non-members to add a book or view all books.

    Prompts the user to press 1 to add a book or press 2 to see all books.
    Calls the appropriate function based on the user's input.

    Parameters:
        None
    
    Returns:
        None
    """
    print("If you want to add a book, press 1")
    print("If you want to see all books, press 2")
    option = int(input())
    if option == 1:
        add_book()
    elif option == 2:
        list_books()

def option_members():
    """
    Presents options for members to add a book, view all books, issue a book, or return a book.

    Prompts the user to press 1 to add a book, press 2 to see all books, press 3 to get a book issued, or press 4 to return a book.
    Calls the appropriate function based on the user's input.

    Parameters:
        None
    
    Returns:
        None
    """
    print("If you want to add a book, press 1")
    print("If you want to see all books, press 2")
    print("If you want to get a book issued, press 3")
    print("If you want to return a book, press 4")
    option = int(input())
    if option == 1:
        add_book()
    elif option == 2:
        list_books()
    elif option == 3:
        issue_book()
    elif option == 4:
        return_book()


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

    Parameters: 
        None
    Returns:
        list_books(pandas.DataFrame) : A pandas dataframe of the list of books in the library

    
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
    Takes the name of the book from the user as input
    and issue it to the user by updating issued status to 'yes'.

    Parameters:
        None
    Returns:
        None

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
    Takes the name of the book from the user as input
    and returns it to the library by updating issued status to 'no'.

    Parameters:
        None
    Returns:
        None

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

def add_member():
        """
        Adds a member into the members.csv file

        Parameters:
            None
        
        Returns:
            None
        """
        
        print("Enter your name:")
        name = input().capitalize()
        print("Enter your email:")
        email = input()
        mem_date = datetime.now()
        print("Enter your preferred membership type: free or premium")
        print("Note, the premium subscription has no fee")
        mem_type = input().capitalize()

        member1 = member.Member(name,email,mem_date,mem_type)
        member1.add_member()

if __name__ == "__main__":
    main()

