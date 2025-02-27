"""
    This class demonstrates various functionalities of the set iterable object in Python.
    Sets are unordered collections of unique elements and support operations such as:
        - Adding and removing elements
        - Set operations (union, intersection, difference, symmetric difference)
        - Checking membership
        - Iterating over elements

    Set is a class which is mutable ,not hashable ,iterable and not a sequenced
    set cannot have duplicate values.
    indexing is not applicable to the set object (slicing operator doesn't work here)
    set doesnot guarantee to store values in the order of insertion
"""
    

class SetDemo:
    
    def __init__(self, elements=None):
        #Initialize set with given elements or an empty set.
        self.elements = set(elements) if elements is not None else set()
    
    def display_set(self):
        #Display set elements.
        print("Set Elements:", self.elements)
    
    def add_element(self, element):
        #Add an element to the set.
        self.elements.add(element)
        print(f"Added {element}:", self.elements)
    
    def remove_element(self, element):
        #Remove an element from the set if it exists.
        self.elements.discard(element)
        print(f"Removed {element}:", self.elements)
    
    def union_sets(self, other_set):
        #Return the union of two sets.
        print("Union:", self.elements.union(other_set))
    
    def intersection_sets(self, other_set):
        #Return the intersection of two sets.
        print("Intersection:", self.elements.intersection(other_set))
    
    def difference_sets(self, other_set):
        #Return the difference between two sets.
        print("Difference:", self.elements.difference(other_set))
    
    
    def check_membership(self, element):
        #Check if an element is present in the set.
        print(f"Is {element} in set?:", element in self.elements)
    
    def iterate_set(self):
        #Iterate over elements in the set.
        print("Iterating over set:")
        for item in self.elements:
            print(item, end=" ")
        print()
    
    def clear_set(self):
        #Clear all elements from the set.
        self.elements.clear()
        print("Set cleared.")


# Demonstrating the SetDemo class
demo = SetDemo({10, 20, 30, 40, 50})
demo.display_set()
demo.add_element(60)
demo.remove_element(20)
demo.union_sets({70, 80, 90})
demo.intersection_sets({30, 40, 100})
demo.difference_sets({30, 50})
demo.check_membership(10)
demo.iterate_set()
demo.clear_set()

#frozen set --> A set is mutable object while frozen set provides an immutable implementation
#concatination and repetition operator not supported in set
#only comparison operator works
#Two set are equal if their elements are same, doesn't matter the order of elements.


#difference between add() and update
#s.add('abc') --> {'abc'}
#s.update('abc') --> {'a','b','c'}  it take only iterable objects
