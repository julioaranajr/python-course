# Python Data Types

## What are Data Types?

Data types are the `classification` or categorization of `data items`. It represents the kind of value that tells what operations can be performed on a particular data. Since `everything is an object in Python programming`, `data types` are actually `classes` and `variables` are `instance (object) of these classes`.

## Data Types in Python

Python has the following data types:

- `int`: Integer values.
- `float`: Floating-point values.
- `str`: String values.
- `bool`: Boolean values.
- `list`: Ordered collection of values.
- `tuple`: Ordered collection of `values that cannot be changed`.
- `set`: `Unordered` collection of `unique values`.
- `dict`: Collection of `key-value pairs`.

### Examples

```python
# Integer
x = 5
print(type(x))  # <class 'int'>

# Float
y = 3.14

# String
z = "Hello, World!"

# Boolean
a = True

# List
b = [1, 2, 3]

# Tuple
c = (1, 2, 3)

# Set
d = {1, 2, 3}

# Dictionary
customer = {"name": "Alice", "age": 30, "DOB": "01/01/1990", "married": True}
```

## How to Check the Data Type of a Variable?

You can use the `type()` function to check the data type of a variable.

### Example

```python
name = "Alice"
print(type(name))  # <class 'str'>
age = 30
print(type(age))  # <class 'int'>
weight = 65.5
print(type(weight))  # <class 'float'>
hobbies = ["reading", "swimming", "cooking"]
print(type(hobbies))  # <class 'list'>
children = {"Alice": 5, "Bob": 3}
print(type(children))  # <class 'dict'>
single = True
print(type(single))  # <class 'bool'>
alice_tuple = ("Alice", 30, 65.5, ["reading", "swimming", "cooking"], {"Alice": 5, "Bob": 3}, True)
print(type(alice_tuple))  # <class 'tuple'>
alice_set = {"Alice", 30, 65.5, "reading", "swimming", "cooking", "Alice", 5, "Bob", 3, True}
print(type(alice_set))  # <class 'set'>
```

## Type Conversion

You can convert one data type to another using the following functions:

- `int()`: Convert to an integer.
- `float()`: Convert to a floating-point number.
- `str()`: Convert to a string.
- `bool()`: Convert to a boolean.
- `list()`: Convert to a list.
- `tuple()`: Convert to a tuple.
- `set()`: Convert to a set.
- `dict()`: Convert to a dictionary.

### Examples

```python
# Convert to an integer
x = int(3.14)
print(x)  # 3

# Convert to a floating-point number
y = float(5)
print(y)  # 5.0

# Convert to a string
z = str(100)
print(z)  # '100'

# Convert to a boolean
a = bool(0)
print(a)  # False
b = bool(1)
print(b)  # True

# Convert to a list
b = list((1, 2, 3))
print(b)  # [1, 2, 3]

# Convert to a tuple
c = tuple([1, 2, 3])
print(c)  # (1, 2, 3)

# Convert to a set
d = set([1, 2, 3])
print(d)  # {1, 2, 3}

# Convert to a dictionary
customer = dict(name="Alice", age=30, DOB="01/01/1990", married=True)
print(customer)  # {'name': 'Alice', 'age': 30, 'DOB': '01/01/1990', 'married': True}
```

## Summary

- Python has several built-in data types, such as `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.
- You can use the `type()` function to check the data type of a variable.
- You can convert one data type to another using the `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, and `dict()` functions.
- Data types are important because they determine what operations can be performed on a particular data.
- Data types are actually classes in Python, and variables are instances (objects) of these classes.

## Additional Resources

- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Type Conversion](https://www.w3schools.com/python/python_casting.asp)
- [Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Data Structures](https://www.w3schools.com/python/python_lists.asp)
