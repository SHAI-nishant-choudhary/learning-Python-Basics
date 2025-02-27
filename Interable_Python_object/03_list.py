"""
    This class demonstrates various functionalities of the list iterable object in Python.
    Lists are mutable, ordered collections that allow duplicate elements.
    Common list operations include:
        - Adding elements (append, insert, extend)
        - Removing elements (remove, pop, clear)
        - Accessing elements (indexing, slicing)
        - Sorting and reversing
        - Iterating over elements
    List is an iterable sequence, mutable and growable
    List can stor hetrogeneous data -> l=[1,1.9,3+4j,"abc",[1,2,3]]
    elements are indexed here
"""

class ListDemo:
    
    def __init__(self, elements=None):
        #Initialize list with given elements or an empty list.
        self.elements = elements if elements is not None else [] #if suppose user doesnot pass any list
    
    def display_list(self):
        #Display list elements.
        print("List Elements:", self.elements)
    
    def add_element(self, element):
        #Add an element to the list.
        self.elements.append(element)
        print(f"Added {element}:", self.elements)
    
    def remove_element(self, element):
        #Remove an element from the list if it exists.
        if element in self.elements:
            self.elements.remove(element)
            print(f"Removed {element}:", self.elements)
        else:
            print(f"Element {element} not found in list.")
    
    def sort_list(self):
        #Sort the list in ascending order.
        self.elements.sort()
        print("Sorted List:", self.elements)
    
    def reverse_list(self):
        #Reverse the order of the list.
        self.elements.reverse()
        print("Reversed List:", self.elements)
    
    def iterate_list(self):
        #Iterate over the list and print elements.
        print("Iterating through list:")
        for item in self.elements:
            print(item, end=" ")
        print()
    
    def get_element(self, index):
        #Retrieve an element by index.
        try:
            print(f"Element at index {index}: {self.elements[index]}")
        except IndexError:
            print("Index out of range.")
    
    def get_length(self):
        print("Length of list :", len(self.elements))
    
    def clear_list(self):
        #Clear all elements from the list.
        self.elements.clear()
        print("List cleared.")

# Demonstrating the ListDemo class

demo = ListDemo([10, 5, 8, 3])
demo.display_list()
demo.add_element(15)
demo.remove_element(5)
demo.sort_list()
demo.reverse_list()
demo.iterate_list()
demo.get_element(2)
demo.get_length()
demo.clear_list()

"""
there are two ways to add a value in list
1) append 
2) insert

"""

l=[1,2,3,4,5]
print(type(l))
l.append(6)  # append method adds value at the end of the list, the new element will become the last element of the list
#[1,2,3,4,5,6]

#l.insert(index,value)
l.insert(2,6)
#if index > last index then value insert at the lastindex+1



#concept of packing and unpacking

#unpacking
l=[1,2,3,4]
a,b,c,d=l #this is unpacking
print(a,b,c,d) #1 2 3 4
#number of varibales in the left hand side must be same as the number of element in a list

#packing
a=3
b=5
c=8
l=[a,b,c] #this is packing

"""
built in method
len(lsit) -> return length of list
min(list) -> return min value in list
max(list) -> return max value in list
sum(list) -> return sum of the list
sorted(list) -> return sorted list of elements
"""


#list() method ->this methodcan take at most argument and if you pass only one argument make sure it must be an iterable one otherwise throw an error
l=list()
l=list(10) # l!=[10] throw an error
l=list(10,20,30) #l!=[10,20,30] throw an error
l=list(range(1,10,1)) #l=[1,2,3,4,5,6,7,8,9]
l=list("Shorthills AI") #l=['S','h','o','r'....]


#Operator on List
# "+" is also known as concatenation operator
l1=[1,2,3]
l2=[9,8,7]
l3=l1+l2 
print(l3) #output : [1,2,3,9,8,7]

# "*" is also known as repetition Operator
l1=[1,2,3]
l2=l1*3
print(l2) #Output : [1,2,3,1,2,3,1,2,3]

#slicing operator in list

#list[beg:end:step]
l=[20,40,10,30,60,50]
#by default step=1
# beg ,end = extreme end 
print(l[2:6:2]) #[10,60]
print(l[4:0:-1]) #[60,30,10,40] 
