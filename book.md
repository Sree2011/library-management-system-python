<!-- markdownlint-disable -->

<a href="./python/src/book.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `book`




**Global Variables**
---------------
- **bookutils**


---

<a href="./python/src/book.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Book`




<a href="./python/src/book.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.__init__`

```python
__init__(name, author, volume, issued)
```

Creates the object of the Book class. 



**Parameters:**
 
 - <b>`name`</b> (str):  The title of the book. 
 - <b>`author`</b> (str):  The author of the book. 
 - <b>`volume`</b> (str):  The volume number of the book. 
 - <b>`issued`</b> (str):  Issued status of the book. 



**Returns:**
 
 - <b>`Book`</b>:  An object of the Book class. 




---

<a href="./python/src/book.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.add_book`

```python
add_book()
```

Adds the book into the library 

This method takes the book's attributes and appends them to a CSV file,  effectively adding the book to the library's records. 



**Parameters:**
  None 



**Returns:**
  None      



---

<a href="./python/src/book.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.find_book`

```python
find_book(name)
```

Finds the book by name from the library 



**Parameters:**
 
 - <b>`name`</b> (str):  The title of the book to be found 



**Returns:**
 
 - <b>`result`</b> (pandas.DataFrame):  A pandas dataframe containing the details of the book 

---

<a href="./python/src/book.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.get_all_books`

```python
get_all_books()
```

Gets the list of all books from the library 



**Parameters:**
  none 



**Returns:**
 
 - <b>`result`</b> (pandas.DataFrame):  A pandas DataFrame containing the details of all books 

---

<a href="./python/src/book.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.issue_book`

```python
issue_book(name)
```

Issues the book and updates the "issued" column to "Yes" 



**Parameters:**
  None 



**Returns:**
  None 

---

<a href="./python/src/book.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.return_book`

```python
return_book(name)
```

Returns the book and updates the "issued" column to "No" 



**Parameters:**
  None 



**Returns:**
  None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
