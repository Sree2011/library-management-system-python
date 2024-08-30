import random
import string
import pandas as pd
import numpy as np
import bookutils
import csv


headings = ["Membership Id", "Name", "Email", "Date of Membership", "Type of Membership"]
#from member import Member
def generate_unique_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.sample(characters, length))
    return random_string

def append_member_to_csv(file_path, my_dict):

    """
       Appends the member details into the members.csv file

       This method takes the member's attributes and appends them to a CSV file, 
       effectively adding the member to the library's records.

        Parameters:
            file_path(str) : File path of the CSV file
            my_dict(dict) : Dictionary containing details of member to be added

        Returns:
            None
    """
    try:
        with open(file_path, 'a', newline='') as file:
            fieldnames = ["id","name","email","member_date","member_type","books_issued"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(my_dict)
            print(f"List appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")

def get_members(file_path):
    """
    Gets the list of all books in the library

    Parameters:
        file_path(str) : File path of the CSV file

    Returns:
        result(numpy.ndarray) : A numpy array containing the details of all books

    """
    try:
        members = pd.read_csv(file_path)
        result = members.to_numpy(dtype=object)
        print(members)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        result = np.array([])
    return result

def find_member(file_path, name):
    """
    Find a book by its name

    Parameters:
        file_path(str) : File path of the CSV file

    Returns:
        result(numpy.ndarray) : A numpy array containing the details of the book found

    """
    
    members = get_members(file_path)
    if members.size == 0:
        return pd.DataFrame(columns=headings)
    
    books_df = pd.DataFrame(members, columns=headings)
    name_lower = name.lower()
    result = books_df[books_df["Name"].str.lower() == name_lower]
    return result

def update_book_issued(file_path, member_name, book_name):
    """
    Updates the issued status of the book based on the input

    Parameters:
        file_path(str) : File path of the CSV file
        name : Name of the book to update the status
        status : The status to update ("Yes" or "No")

    Returns:
        None
    """
    members = []
    try:
        with open(file_path, 'a', newline='') as file:
            fieldnames = ["Member id","Member name","Book issued"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            result = find_member(member_name)
            print(result)
            my_dict = {"Member id":result["Membership Id"],"Member name":member_name,"Book issued":book_name}
            writer.writerow(my_dict)
            print(f"List appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}") 
e = find_member("./python/data/members.csv","Potter")
print(e,type(e))