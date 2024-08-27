<!-- markdownlint-disable -->

<a href=".\book#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `book`




**Global Variables**
---------------
- **bookutils**


---

<a href=".\book\Book#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Book`




<a href=".\book\__init__#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.__init__`

```python
__init__(name, author, volume, issued)
```

Creates the object of book class 

Parameters 
---------- 

name : str  The title of the book. author : str  The author of the book. volume : str  The volume number of the book. issued : str  Issued status of the book. 

 

Returns 
------- Book  An object of the book class. 




---

<a href=".\book\add_book#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.add_book`

```python
add_book()
```

Add a new book to the library. 

Parameters 
---------- name : str  The title of the book. 



 

Returns 
------- bool  True if the book was added successfully, False otherwise. 

---

<a href=".\book\find_book#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.find_book`

```python
find_book(name)
```

Finds the book by name from the library 

Parameters 
---------- 

name : str  The title of the book 

 

Returns 
------- result : A pandas DataFrame   A dataframe containing all fields of the book found 

---

<a href=".\book\get_all_books#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.get_all_books`

```python
get_all_books()
```

Gets the list of all books from the library 

Parameters 
---------- None 



Returns 
------- result : A pandas DataFrame  A dataframe containing all fields of all the books in the library 

---

<a href=".\book\issue_book#L100"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.issue_book`

```python
issue_book(name)
```

Issues the book and updates the "issued" column to "Yes" 

Parameters 
---------- 

name : str  The title of the book  



Returns 
------- None 

---

<a href=".\book\return_book#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Book.return_book`

```python
return_book(name)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
