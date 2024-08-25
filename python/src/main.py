import book
import pandas as pd
import numpy as np

def main():
    print("Hi! Welcome to our Library Management System!")
    name_user = input("What should we call you? ")
    print(f"Hello, {name_user}")
    print("If you want to add a book, press 1")
    print("If you want to see all books, press 2")
    print("If you want to get a book issued, press 3")
    print("If you want to return a book, press 4")

    option_book = int(input())
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
    print("Enter the details of the book you want to add:")
    name_book = input("Enter name: ").capitalize()
    author_book = input("Enter author: ").capitalize()
    volume_book = input("Enter volume number of the book (Eg. 1st): ")
    issued = "No"
    new_book = book.Book(name_book, author_book, volume_book, issued)
    new_book.add_book()

def list_books():
    sample_book = book.Book("nn", "88", "4th", "Yes")
    columns = ["Name", "Author", "Volume", "Issued"]
    books = sample_book.get_all_books()
    list_books = pd.DataFrame(books, columns=columns)
    list_books.index = np.arange(1, len(list_books) + 1)
    print(list_books)
    return list_books

def issue_book():
    df = list_books()
    name = input("Enter the name of the book you want to be issued: ").capitalize()
    result = df[df["Name"].str.lower() == name.lower()]
    
    if result.empty:
        print("No books found with that name.")
    else:
        print("Books found:")
        print(result)
        # Assuming issue_book method updates the book's issued status
        sample_book = book.Book(result.iloc[0]["Name"], result.iloc[0]["Author"], result.iloc[0]["Volume"], result.iloc[0]["Issued"])
        sample_book.issue_book(name)

def return_book():
    # Implement the return book functionality here
    pass

if __name__ == "__main__":
    main()
