"""
    Range is similiar with Arthimetic Progression (AP)
    This class demonstrates various functionalities of the range iterable object in Python.
    The range() function is used to generate a sequence of numbers.
    Syntax:
        - range(stop): Generates numbers from 0 to (stop-1).
        - range(start, stop): Generates numbers from start to (stop-1).
        - range(start, stop, step): Generates numbers from start to (stop-1) with step intervals.
    Range is immutable sequence and contain only int tpes value
"""
class RangeDemo: 
    def __init__(self, start=0, stop=10, step=1):
        #Initialize range parameters.
        self.start = start
        self.stop = stop
        self.step = step
        self.range_obj = range(self.start, self.stop, self.step)
    
    def display_range(self):
        #Display range elements as a list.
        print(f"Range({self.start}, {self.stop}, {self.step}):", list(self.range_obj))
    
    def range_length(self):
        #Return the length of the range.
        print("Length of range:", len(self.range_obj))
    
    def check_element(self, element):
        #Check if an element is present in the range.
        print(f"Is {element} in range?", element in self.range_obj) #here we use in operator
    
    def iterate_range(self):
        #Iterate over range using a for loop.
        print("Iterating over range:")
        for num in self.range_obj:
            print(num, end=" ")
        print() #for next line
    
    def get_index_value(self, index):
        #Retrieve a value by its index in the range.
        try:
            print(f"Value at index {index}:", self.range_obj[index])
        except IndexError:
            print("Index out of range.") #if index is greater and equal to the len(range)
    
    def reverse_range(self):
        #Reverse the range sequence.
        print("Reversed range:", list(reversed(self.range_obj)))
    
    def step_function(self, new_step):
        #Create a new range object with a different step value.
        print(f"New range with step {new_step}:", list(range(self.start, self.stop, new_step)))

# Demonstrating the RangeDemo class

demo = RangeDemo(1, 20, 2)
demo.display_range()
demo.range_length()
demo.check_element(5)
demo.iterate_range()
demo.get_index_value(3)
demo.reverse_range()
demo.step_function(3)

"""
This program demonstrates:

1) Creating a range object in an OOP manner.
2) Displaying the range as a list.
3) Checking the length of the range.
4) Checking if an element exists in the range.
5) Iterating over a range.
6) Accessing an element by index.
7) Reversing a range.
8) Creating a range with a different step value.

"""
