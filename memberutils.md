<!-- markdownlint-disable -->

<a href="./python/src/memberutils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `memberutils`




**Global Variables**
---------------
- **headings**

---

<a href="./python/src/memberutils.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `generate_unique_random_string`

```python
generate_unique_random_string(length)
```






---

<a href="./python/src/memberutils.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `append_member_to_csv`

```python
append_member_to_csv(file_path, my_dict)
```

Appends the member details into the members.csv file 

This method takes the member's attributes and appends them to a CSV file,  effectively adding the member to the library's records. 



**Parameters:**
 
  - <b>`file_path(str) `</b>:  File path of the CSV file 
  - <b>`my_dict(dict) `</b>:  Dictionary containing details of member to be added 



**Returns:**
 None 


---

<a href="./python/src/memberutils.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_members`

```python
get_members(file_path)
```

Gets the list of all books in the library 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 



**Returns:**
 
 - <b>`result(numpy.ndarray) `</b>:  A numpy array containing the details of all books 


---

<a href="./python/src/memberutils.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `find_member`

```python
find_member(file_path, name)
```

Find a book by its name 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 



**Returns:**
 
 - <b>`result(numpy.ndarray) `</b>:  A numpy array containing the details of the book found 


---

<a href="./python/src/memberutils.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_book_issued`

```python
update_book_issued(file_path, member_name, book_name)
```

Updates the issued status of the book based on the input 



**Parameters:**
 
 - <b>`file_path(str) `</b>:  File path of the CSV file 
 - <b>`name `</b>:  Name of the book to update the status 
 - <b>`status `</b>:  The status to update ("Yes" or "No") 



**Returns:**
 None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
