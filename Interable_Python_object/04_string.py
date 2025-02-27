"""
    This class demonstrates various functionalities of the string iterable object in Python.
    Strings are immutable sequences of characters and support various operations such as:
        - Accessing elements (indexing, slicing)
        - Modifying (concatenation, repetition, case conversion)
        - Searching and replacing
        - Checking properties (isalpha, isdigit, startswith, endswith)
        - Iterating over characters
    Str is a class which is immutable ,iterable and hashable
    Str is a sequence iterable
"""

class StringDemo:
    
    def __init__(self, text="Hello, World!"):
        #Initialize string with a default or given value.
        self.text = text
    
    def display_string(self):
        #Display the string.
        print("String:", self.text)
    
    def string_length(self):
        #Return the length of the string.
        print("Length of string:", len(self.text))
    
    def concatenate(self, other_text):
        #Concatenate another string to the current string.
        print("Concatenated String:", self.text + other_text)
    
    def repeat_string(self, times):
        #Repeat the string a given number of times.
        print("Repeated String:", self.text * times)
    
    def convert_case(self):
        #Convert the string to uppercase and lowercase.
        print("Uppercase:", self.text.upper())
        print("Lowercase:", self.text.lower())
    
    def check_substring(self, substring):
        #Check if a substring exists in the string.
        print(f"Is '{substring}' in string?:", substring in self.text)
    
    def iterate_string(self):
        #Iterate over characters in the string.
        print("Characters in string:")
        for char in self.text:
            print(char, end=" ")
        print()
    
    def replace_substring(self, old, new):
        #Replace a substring with another substring.
        print("Replaced String:", self.text.replace(old, new))
    
    def split_string(self, delimiter=" "):
        #Split the string into a list based on a delimiter.
        print("Split String:", self.text.split(delimiter))

# Demonstrating the StringDemo class

demo = StringDemo("Python Programming")
demo.display_string()
demo.string_length()
demo.concatenate(" is fun!")
demo.repeat_string(2)
demo.convert_case()
demo.check_substring("Python")
demo.iterate_string()
demo.replace_substring("Programming", "Scripting")
demo.split_string()



#how to create str object
s="Shorthills AI"
s='Gurgaon'
s="""Hello World"""
s='''Hello World'''
s=str(124) #s="124"
s=str() #s=""

#operator in str
#concatenation operator
s1="Hello "
s2="World"
s3=s1+s2
print(s3) # "Hello World"

#Repetition Operator
s1="Hello World"
s2= s1*3
print(s2) # "Hello WorldHello WorldHello World"

#comparison operator 
# s1 > s2 ->true if s1 comes after s2 in dictionary order

#str object methods
"""
index(),count()
startwith(), endwith()
split()
join()
isdigit()
islower()
isupper()
lower()
upper()
replace()  # s="ShorthillsAi"
#s.replace('i','I') --> "ShorthIllsAI"
"""


#split and join method
#split --> return list
s="Hey my name is Nishant Choudhary"
l=s.split(" ");
print(l) #l = ["Hey","my","name","is","Nishant","Choudhary"]

#join --> it return string
l=["hello","My","Self"]
s=" ".join(l)
print(s) #return "hello My Self"
