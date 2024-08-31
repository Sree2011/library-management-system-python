"""
Member Module

This module provides functionalities to manage a library system, including member management, issuing book to a member and returning a book from member.
Modules:

    memberutils: 
        Utility functions for handling member data operations such as appending to CSV, finding members, and updating member status.

Classes:

    Member: 
        Represents a member in the library and provides methods to add, update, delete members.

Functions:

    add_member():
        Adds a member to the library
    
    update_member():
        Update the books issued to the member

    delete_member():
        Delete a member

"""

import memberutils
#from datetime import datetime
class Member:
    def __init__(self,name,email,member_date,member_type):
        self.id = memberutils.generate_unique_random_string(10)
        self.name = name
        self.email = email
        self.member_date = member_date
        self.member_type = member_type

    def add_member(self):
        """
        Adds a member to the library

        Parameters:
            None

        Returns:
            None
        """
        book_array = self.__dict__
        memberutils.append_dict_to_csv("./python/data/members.csv", book_array)
        print("Member Added:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Added on: {self.member_date}")
        print(f"Membership Type: {self.member_type}")

    def issue_book(self,name):
        pass

    def find_member(self,name):
        return memberutils.find_member("./python/data/members.csv",name)