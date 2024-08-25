import csv

import numpy as np
import pandas as pd
book = [[]]
def append_dict_to_csv(file_path, my_dict):
    try:
        with open('./python/data/books.csv', 'a', newline='') as file:
            fieldnames = ['name','author','volume','issued']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Append the dictionary
            writer.writerow(my_dict)
            print(f"List appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

def get_books():
    books = pd.read_csv("./python/data/books.csv")
    hint = books.to_numpy(dtype=object)
    print(hint)
    return hint

def issue_book(name):
    books = get_books()
    books = np.array(books, dtype=object)
    
    positions = np.argwhere(books[:, 0] == name)
    
    if len(positions) > 0:
        try:
            print(positions[0][0], positions[0][1])
            book_pos = positions[0][0]
            books[book_pos][3] = True
            np.savetxt('./python/data/books.csv', books, delimiter=',', fmt='%s')
            print(f"Book '{name}' has been issued.")
        except Exception as e:
            print("Error: ", e)
    else:
        print("Sorry, Book not found! Would you like to add that? Enter yes or no")
        option = input()
        if option.lower() == "yes":
            
            print("Enter author:")
            author = input()
            print("Enter volume no:")
            volume = input()
            issued = True
            new_book = [name, author, volume, issued]
            books = np.append(books, [new_book], axis=0)
            np.savetxt('./python/data/books.csv', books, delimiter=',', fmt='%s')
            print(f"Book Added:\nName: {name}\nAuthor: {author}\nVolume: {volume}\nIssued: {issued}")
        elif option.lower() == "no":
            print("Thank you!")
