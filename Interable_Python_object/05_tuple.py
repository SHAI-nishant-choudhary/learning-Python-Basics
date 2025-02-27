"""
    This class demonstrates various functionalities of the tuple iterable object in Python.
    Tuples are immutable sequences that support various operations such as:
        - Accessing elements (indexing, slicing)
        - Counting occurrences of an element
        - Finding the index of an element
        - Concatenation and repetition
        - Iterating over elements
    
    Tuple is a class ,which is iterable ,immutable and hasbale
    it is a sequence(order maintain same as the order of insertion)
"""

class TupleDemo:
    
    def __init__(self, elements=(1, 2, 3, 4, 5)):
        #Initialize tuple with given elements or a default tuple.
        self.elements = elements
    
    def display_tuple(self):
        #Display tuple elements.
        print("Tuple Elements:", self.elements)
    
    def tuple_length(self):
        #Return the length of the tuple.
        print("Length of tuple:", len(self.elements))
    
    def access_element(self, index):
        #Access an element by index.
        try:
            print(f"Element at index {index}: {self.elements[index]}")
        except IndexError:
            print("Index out of range.")
    
    def count_occurrences(self, value):
        #Count occurrences of a specific value in the tuple.
        print(f"Occurrences of {value}: {self.elements.count(value)}")
    
    def find_index(self, value):
        #Find the index of a value in the tuple.
        try:
            print(f"Index of {value}: {self.elements.index(value)}")
        except ValueError:
            print(f"{value} not found in tuple.")
    
    def iterate_tuple(self):
        #Iterate over elements in the tuple.
        print("Iterating over tuple:")
        for item in self.elements:
            print(item, end=" ")
        print()
    
    def concatenate_tuple(self, other_tuple):
        #Concatenate another tuple to the current tuple.
        print("Concatenated Tuple:", self.elements + other_tuple)
    
    def repeat_tuple(self, times):
        #Repeat the tuple a given number of times.
        print("Repeated Tuple:", self.elements * times)

# Demonstrating the TupleDemo class
demo = TupleDemo((10, 20, 30, 40, 50, 10))
demo.display_tuple()
demo.tuple_length()
demo.access_element(2)
demo.count_occurrences(10)
demo.find_index(30)
demo.iterate_tuple()
demo.concatenate_tuple((60, 70, 80))
demo.repeat_tuple(2)



#Working of tuple on various operator

#slicing operator
t=(1,2,3,4,5)
#t[beg:end:step]
print(t[::-1]) #print it in reverse order

t=sorted(t) #it will not change in given tuple it just return another tuple in sorted order

