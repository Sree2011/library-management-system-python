<!-- markdownlint-disable -->

<a href="./python/src/bookutils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `bookutils`
BookUtils Module 

This module provides utility functions to manage a library system, including book management, tracking the issue and return of books, and updating book statuses. 

Modules : 

 csv :   Python library for handling csv files 

 numpy :  Python library for data analysis 

 pandas :  Python library for data visualization 

Functions : 

 append_dict_to_csv(file_path, my_dict) :  Appends the dictionary my_dict as a new row into the file path. 

 get_books(file_path) :  Reads all the rows from the file. 

 find_book(file_path, name) :  Searches in the file by name. 

 update_book_status(file_path, name, status) :  Updates the issued column of the name with the status. 


---

<a href="./python/src/bookutils.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `append_dict_to_csv`

```python
append_dict_to_csv(file_path, my_dict)
```

Appends the book details into the books.csv file 

This method takes the book's attributes and appends them to a CSV file,  effectively adding the book to the library's records. 



**Parameters:**
 
  - <b>`file_path(str) `</b>:  File path of the CSV file 
  - <b>`my_dict(dict) `</b>:  Dictionary containing details of book to be added 



**Returns:**
 None 


---

<a href="./python/src/bookutils.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_books`

```python
get_books(file_path)
```

Gets the list of all books in the library 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 



**Returns:**
 
 - <b>`result(numpy.ndarray) `</b>:  A numpy array containing the details of all books 


---

<a href="./python/src/bookutils.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_book`

```python
find_book(file_path, name)
```

Find a book by its name 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 



**Returns:**
 
 - <b>`result(numpy.ndarray) `</b>:  A numpy array containing the details of the book found 


---

<a href="./python/src/bookutils.py#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_book_status`

```python
update_book_status(file_path, name, status)
```

Updates the issued status of the book based on the input 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 
 - <b>`name(str) `</b>:  Name of the book to update the status 
 - <b>`status(str) `</b>:  The status to update ("Yes" or "No") 



**Returns:**
 None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
