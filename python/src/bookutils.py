import csv
import numpy as np
import pandas as pd

def append_dict_to_csv(file_path, my_dict):
    try:
        with open(file_path, 'a', newline='') as file:
            fieldnames = ['name', 'author', 'volume', 'issued']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(my_dict)
            print(f"List appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

def get_books(file_path):
    try:
        books = pd.read_csv(file_path)
        return books.to_numpy(dtype=object)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return np.array([])

def find_book(file_path, name):
    books = get_books(file_path)
    if books.size == 0:
        return pd.DataFrame(columns=["Name", "Author", "Volume", "Issued"])
    
    books_df = pd.DataFrame(books, columns=["Name", "Author", "Volume", "Issued"])
    name_lower = name.lower()
    result = books_df[books_df["Name"].str.lower() == name_lower]
    return result

def update_book_status(file_path, name, status):
    books = np.genfromtxt(file_path, delimiter=',', dtype=str, skip_header=1)
    name_lower = name.lower()
    positions = np.argwhere(np.char.lower(books[:, 0]) == name_lower)
    for pos in positions:
        books[pos[0], 3] = status
    np.savetxt(file_path, books, delimiter=',', fmt='%s', header='Name,Author,Volume,Issued', comments='')