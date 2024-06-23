# Python Variables

## What are variables?

Variables are used to `store data in a program`. They are like `containers` that hold values that can be used in calculations, comparisons, and other operations.

## Variables in Python

In Python, variables are created by assigning a value to a name. The name of a variable can contain letters, numbers, and underscores, `but it cannot start with a number`. Variable names are `case-sensitive`.

```python
x = 5
y = "Hello, World!"
```

Variables can be reassigned to `new values`:

```python
x = 10
y = "Goodbye, World!"
```

Variables can also be used in expressions:

```python
z = x + 5
print(z)
```

Variables can store different types of data, such as `integers`, `floats`, `strings`, and `booleans`:

```python
a = 5
b = 3.14
c = "Hello, World!"
d = True
```

Variables can be used to store the results of `calculations`:

```python
length = 10
width = 5
area = length * width
print(area)
```

Variables can be used to store the results of `functions`:

```python
def add(x, y):
    return x + y
result = add(3, 5)
print(result)
```

Variables can be used to store the results of `comparisons`:

```python
x = 5
y = 10
is_greater = x > y
print(is_greater)
```

Variables can be used to store the results of `logical operations`:

```python
x = True
y = False
result = x and y
print(result)
```

Variables can be used to store the results of `conditional statements`:

```python
x = 5
if x > 0:
    print("Positive")
else:
    print("Negative")
```

Variables can be used to store the results of `loops`:

```python
for i in range(5):
    print(i)
```

Variables can be used to store the results of `functions`:

```python
def add(x, y):
    return x + y
result = add(3, 5)
print(result)
```

## Naming Conventions

When naming variables, it is important to follow `naming conventions` to make the code more readable and maintainable. Here are some common naming conventions for variables in Python:

- Use `descriptive names` that indicate the purpose of the variable.
- Use `lowercase letters` for variable names.
- Use `underscores` to separate words in variable names.
- Use `camelCase` for variable names in classes and functions.
- Use `all uppercase letters` for constants.
- Avoid using `reserved words` as variable names.
- Avoid using `single-letter variable names` except for loop counters.
- Use `singular names` for variables that store a single value and `plural names` for variables that store multiple values.
- Use `meaningful names` that describe the data stored in the variable.
- Use `consistent naming conventions` throughout the codebase.
- Use `self-explanatory names` that make the code easier to understand.
- Use `short names` for temporary variables and `long names` for variables with a wider scope.
- Use `meaningful prefixes` for variables that store specific types of data.
- Use `meaningful suffixes` for variables that store specific types of data.
- Use `meaningful abbreviations` for variables that store specific types of data.

### Examples of variable names:

```python
first_name = "John"
last_name = "Doe"
total_amount = 100.50
is_valid = True
MAX_VALUE = 1000
counter = 0
students = ["Alice", "Bob", "Charlie"]  
```

## Summary

Variables are used to store data in a program. They are like containers that hold values that can be used in calculations, comparisons, and other operations.

In Python, variables are created by assigning a value to a name. Variable names can contain letters, numbers, and underscores, but they cannot start with a number. 

Variable names are case-sensitive. It is important to follow naming conventions when naming variables to make the code more readable and maintainable.

Variables can store different types of data, such as integers, floats, strings, and booleans. They can be used in expressions, calculations, comparisons, logical operations, conditional statements, loops, functions, and more.

## Additional Resources

- [Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Naming Conventions](https://pep8.org/#naming-conventions)
- [Python Variable Names](https://www.programiz.com/python-programming/variables-constants-literals)
