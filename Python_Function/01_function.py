"""
In Python, a function is a reusable block of code that performs a specific task. Functions help in organizing code, improving readability, and avoiding repetition.

Defining a Function
A function is defined using the `def` keyword followed by the function name and parentheses `()`.

"""
#Syntax
def function_name(parameters):
    # Function body (code to execute)
    return parameters  # (Optional) return statement


#Example: A Simple Function
def greet(name):
    #This function greets the user by name.
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


#Types of Functions

#1. Built-in Functions  
#Python provides many built-in functions like `print()`, `len()`, `max()`, `sum()`, etc.
print(len("Python"))  # Output: 6

#2. User-defined Functions
#These are functions created by the user using `def`.
def add(a, b):
    return a + b
print(add(3, 5))  # Output: 8


#3.Lambda Functions (Anonymous Functions) 
#  A function without a name, defined using the `lambda` keyword.

square = lambda x: x * x
print(square(4))  # Output: 16


#4.Recursive Functions 
   #A function that calls itself.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

"""
Function Parameters
    Positional Arguments Order matters.
    Keyword Arguments Specified by name.
    Default Parameters Provide default values.
    Variable-length Arguments Accept multiple arguments (`*args`, `**kwargs`).
"""


def greet(name, message="Welcome!"):
    return f"{message}, {name}"

print(greet("Alice"))          # Output: Welcome!, Alice
print(greet("Bob", "Hello"))   # Output: Hello, Bob

