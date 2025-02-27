#Iterable
"""
    Iterables in Python
        An iterable is any Python object that can return its elements one at a time. In simple terms, 
        an iterable is an object that can be iterated over using a loop.

Types of Iterables in Python
There are several types of iterables:

1. Sequences
   - These are ordered collections of elements that support indexing and slicing.
   - Examples 
     - list → [1, 2, 3, 4]
     - tuple → (1, 2, 3, 4)
     - str → "hello"

2. Non-Sequences (Iterator-Based)
   - These are objects that do not support direct indexing but can still be iterated over.
   - Examples:
     - set → {1, 2, 3, 4}
     - dict → {"a": 1, "b": 2}
     - Generator objects → Created using yield or generator expressions

3. Custom Iterables
   - You can create your own iterable class by defining the __iter__() and __next__() methods.

"""

# List (Sequence)
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)  # Iterating over a list

# String (Sequence)
my_string = "Hello"
for char in my_string:
    print(char)  # Iterating over a string

# Dictionary (Non-Sequence)
my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key, my_dict[key])  # Iterating over a dictionary

# Generator (Custom Iterable)
def my_generator():
    for i in range(3):
        yield i  # Yielding values one at a time

gen = my_generator()
for value in gen:
    print(value)  # Iterating over a generator
