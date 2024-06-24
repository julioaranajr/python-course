# Python Data Types

## What are Python Data Types?

Data types are the classification or categorization of data items. In Python, every value has a data type, and every variable has a data type. Python has the following data types built-in by default:

- Text Type: `str`
- Numeric Types: `int`, `float`, `complex`
- Sequence Types: `list`, `tuple`, `range`
- Mapping Type: `dict`
- Set Types: `set`, `frozenset`
- Boolean Type: `bool`
- Binary Types: `bytes`, `bytearray`, `memoryview`

## How to determine the Data Type of a Value?

You can use the `type()` function to determine the data type of a value. For example:

```python
x = 5
y = "Hello, World!"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
```

## Why are Python Data Types important?

Data types are important because they define the operations that can be performed on the values. For example, you can perform arithmetic operations on numeric types (`int`, `float`, `complex`), but not on text types (`str`).

By understanding the data types in Python, you can write more efficient and error-free code. You can also use the appropriate data types to represent the data in your programs, which can improve the readability and maintainability of your code.

<br>

## << Previous: [Variables](1B-variables.md) | Next: [Numbers](1D-numbers.md) >>
