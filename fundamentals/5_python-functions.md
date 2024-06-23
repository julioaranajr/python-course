# Python functions

## What are Functions?

A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Why use functions?

Functions are used to `organize code`, `reduce redundancy`, `improve readability`, and `encapsulate logic`. They are especially useful when you need to perform the same operation multiple times or when you want to break down a complex problem into smaller, more manageable parts.

## How do functions work?

1. Define a function using the `def` keyword. 
    - The function definition includes the function name, parameters, and body of the function.
    - e.g., `def my_function():`.
2. Call the function using the function name followed by parentheses. 
    - e.g., `my_function()`.
    - The function call executes the code inside the function.
3. Pass arguments to the function if needed.
    - Arguments are the data you pass into the function's parameters.
    - e.g., `greet("Alice")`.
4. Return a value from the function if needed.
    - Use the `return` keyword to return a value from the function.
    - e.g., `return x + y`.
5. Use the return value in an expression or assign it to a variable.
    - e.g., `result = add(3, 5)`.

### Examples

```python
def my_function():
    print("Hello, World!")

my_function()  # Hello, World!
```

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
```

```python
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # 8
```

## How to define a function?

The function name is the name of the function that you define.

It is used to call the function and execute the code inside the function. e.g.:

```python
def my_function(): # def is the keyword used to define a function, my_function is the function name
    print("Hello from a function")
```

We will see keywords later in this repository. For now, just remember that `def` is the keyword used to define a function.

## What is a parameter?

A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. e.g.:

```python
def greet(name): # greet is the function and name is the parameter
    print(f"Hello, {name}!")

greet("Alice") # we call the greet function and "Alice" is the argument
```

## What is an argument?

An argument is the actual value that is passed to the function when it is called. e.g.:

```python
def greet(name): # name is the parameter
    print(f"Hello, {name}!")

greet("Alice")  # "Alice" is the argument passed to the greet function
```

## What is a return value?

A return value is the value that a function returns when it is called. It is the result of the function's computation. e.g.:

```python
def add(x, y):
    return x + y # return the sum of x and y

result = add(3, 5) # 3 + 5 = 8
print(result)  # 8
```

## How to call a function?

To call a function, use the function name followed by parentheses:

```python
my_function()
```

## When to use functions?

Functions are used to `organize code`, `reduce redundancy`, `improve readability`, and `encapsulate logic`. They are especially useful when you need to perform the same operation multiple times or when you want to break down a complex problem into smaller, more manageable parts.

## Summary

- A function is a block of code that only runs when it is called.
- Functions are used to `organize code`, `reduce redundancy`, `improve readability`, and `encapsulate logic`.
- You can define a function using the `def` keyword.
- You can call a function using the function name followed by parentheses.
- You can pass data, known as parameters, into a function.
- A function can return data as a result.
- Use the `return` keyword to return a value from the function.
- Use the return value in an expression or assign it to a variable.

## Additional Resources

- [Python Functions - Python.org](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Functions - W3Schools](https://www.w3schools.com/python/python_functions.asp)
- [Python Functions - Real Python](https://realpython.com/defining-your-own-python-function/)
- [Python Functions - Programiz](https://www.programiz.com/python-programming/function)
- [Python Functions - GeeksforGeeks](https://www.geeksforgeeks.org/functions-in-python/)
- [Python Functions - Tutorialspoint](https://www.tutorialspoint.com/python/python_functions.htm)
- [Python Functions - DataCamp](https://www.datacamp.com/community/tutorials/functions-python-tutorial)
