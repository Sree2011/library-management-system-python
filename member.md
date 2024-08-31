<!-- markdownlint-disable -->

<a href="./python/src/member.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `member`
Member Module 

This module provides functionalities to manage a library system, including member management, issuing book to a member and returning a book from member. Modules: 

 memberutils:   Utility functions for handling member data operations such as appending to CSV, finding members, and updating member status. 

Classes: 

 Member:   Represents a member in the library and provides methods to add, update, delete members. 

Functions: 

 add_member():  Adds a member to the library  

 update_member():  Update the books issued to the member 

 delete_member():  Delete a member 

**Global Variables**
---------------
- **memberutils**


---

<a href="./python/src/member.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Member`




<a href="./python/src/member.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Member.__init__`

```python
__init__(name, email, member_date, member_type)
```








---

<a href="./python/src/member.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Member.add_member`

```python
add_member()
```

Adds a member to the library 



**Parameters:**
  None 



**Returns:**
  None 

---

<a href="./python/src/member.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Member.find_member`

```python
find_member(name)
```





---

<a href="./python/src/member.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Member.get_all_members`

```python
get_all_members()
```

Gets the list of all members in the library as a pandas dataframe 



**Parameters:**
  None 



**Returns:**
 
 - <b>`dh(pandas.DataFrame) `</b>:  A dataframe containing the details of all members 

---

<a href="./python/src/member.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Member.issue_book`

```python
issue_book(name)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
