<!-- markdownlint-disable -->

<a href="./python/src/bookutils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `bookutils`
BookUtils Module 

This module provides utility functions to manage a library system, including book management, tracking the issue and return of books, and updating book statuses. 



Functions:  append_dict_to_csv(file_path,my_dict): Appends the dictionary my_dict as a new row into the file path  get_books(file_path): Reads all the rows from the file  find_book(file_path,name): Searches in the file by name  update_book_status(file_path,name,status): Updates the issued column of the name with the status 

Modules:  csv: Python library for handling csv files  numpy: Python library for data analysis  pandas: Python library for data visualisation 


---

<a href="./python/src/bookutils.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `append_dict_to_csv`

```python
append_dict_to_csv(file_path, my_dict)
```






---

<a href="./python/src/bookutils.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_books`

```python
get_books(file_path)
```






---

<a href="./python/src/bookutils.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_book`

```python
find_book(file_path, name)
```






---

<a href="./python/src/bookutils.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_book_status`

```python
update_book_status(file_path, name, status)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
