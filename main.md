<!-- markdownlint-disable -->

<a href="./python/src/main.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `main`
Main Module 

This module provides an interactive interface to the user 

Modules: 

 book:   functionalities to manage a library system, including book management, tracking the issue and return of books, and updating book statuses  

 pandas:  Python library for data visualisation  

 numpy:  Python library for data analysis 



Functions: 

 option_non_members():  Presents options for non-members to add a book or view all books. 

 option_members():  Presents options for members to add a book, view all books, issue a book, or return a book. 

 add_book():   Adds a new book to the library. 

 find_book(name):   Finds a book by its title. 

 list_books():   Retrieves a list of all books in the library. 

 issue_book(name):   Issues a book and updates its status to "Yes".  

 return_book(name):   Returns a book and updates its status to "No". 


---

<a href="./python/src/main.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main()
```

Display welcome information to the user and do the operation based on the user's preference 



**Parameters:**
  None 

**Returns:**
  None 


---

<a href="./python/src/main.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `option_non_members`

```python
option_non_members()
```

Presents options for non-members to add a book or view all books. 

Prompts the user to press 1 to add a book or press 2 to see all books. Calls the appropriate function based on the user's input. 


---

<a href="./python/src/main.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `option_members`

```python
option_members()
```

Presents options for members to add a book, view all books, issue a book, or return a book. 

Prompts the user to press 1 to add a book, press 2 to see all books, press 3 to get a book issued, or press 4 to return a book. Calls the appropriate function based on the user's input. 


---

<a href="./python/src/main.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_book`

```python
add_book()
```

Take the details of the book from the user as input and add them to the library file. 



**Parameters:**
  None 

**Returns:**
  None 


---

<a href="./python/src/main.py#L153"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `list_books`

```python
list_books()
```

Lists all the books available in the library. 



**Parameters:**
  None 

**Returns:**
 
 - <b>`list_books(pandas.DataFrame) `</b>:  A pandas dataframe of the list of books in the library 


---

<a href="./python/src/main.py#L186"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `issue_book`

```python
issue_book()
```

Takes the name of the book from the user as input and issue it to the user by updating issued status to 'yes'. 



**Parameters:**
  None 

**Returns:**
  None 


---

<a href="./python/src/main.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `return_book`

```python
return_book()
```

Takes the name of the book from the user as input and returns it to the library by updating issued status to 'no'. 



**Parameters:**
  None 

**Returns:**
  None 


---

<a href="./python/src/main.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_member`

```python
add_member()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
