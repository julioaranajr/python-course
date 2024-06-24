# Python Syntax

## Python Syntax Compared to Other programming Languages

Python was designed to be easy to read and write. Here is a simple example of Python code:

```python
print("Hello, World!")
```

Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.

Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

## Executing Python Syntax

As we learned in the previous point, Python syntax can be executed by writing directly in the Command Line:

```bash
> python3 -c "print('Hello, World!')"
```

Or by creating a python file on the command line:

```bash
> echo "print('Hello, World!')" > hello.py
> python3 hello.py
```

## Python Indentation

Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, in Python the indentation is very important.

Python uses indentation to indicate a block of code. For example:

```python
if 2 + 2 == 4:
    print("Correct")
```

The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

you can use tabs or spaces, but not both in the same block of code.

if you use spaces, Python will not allow for the use of 4 spaces in one block and 3 spaces in another block. The code will not execute properly.

## Syntax Rules

Python has the following syntax rules:

- Python is case-sensitive
- Python statements must end with a newline character
- Python uses indentation to define code blocks
- Python uses the `#` symbol to indicate comments
- Python uses the `:` symbol to indicate the start of a code block
- Python uses the `=` symbol to assign values to variables
- Python uses the `+`, `-`, `*`, `/`, and `%` symbols for arithmetic operations
- Python uses the `==`, `!=`, `>`, `<`, `>=`, and `<=` symbols for comparison operations
- Python uses the `and`, `or`, and `not` keywords for logical operations
- Python uses the `if`, `else`, and `elif` keywords for conditional statements
- Python uses the `for` and `while` keywords for loops
- Python uses the `def` keyword to define functions
- Python uses the `class` keyword to define classes
- Python uses the `import` keyword to import modules
- Python uses the `from` keyword to import specific parts of a module
- Python uses the `as` keyword to create an alias for a module or variable
- Python uses the `return` keyword to return a value from a function
- Python uses the `pass` keyword as a placeholder
- Python uses the `break` keyword to exit a loop
- Python uses the `continue` keyword to skip the rest of the code in a loop and start the next iteration
- Python uses the `global` keyword to declare a global variable
- Python uses the `nonlocal` keyword to declare a nonlocal variable
- Python uses the `assert` keyword to check if a condition is true
- Python uses the `try`, `except`, and `finally` keywords to handle exceptions
- Python uses the `raise` keyword to raise an exception
- Python uses the `with` keyword to simplify exception handling
- Python uses the `yield` keyword to return a generator

You can not use these keywords as variable names or part of a variable name. if you do, you will get an error. Also, you can not use special characters in variable names.

<br>

## << Previous: [Get Started](01_get_started.md) | Next: [Python Comments](1A-comments.md) >>
