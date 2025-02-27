"""
    This class demonstrates various functionalities of the dictionary (dict) iterable object in Python.
    Dictionaries store key-value pairs and support operations such as:
        - Adding and updating key-value pairs
        - Removing elements
        - Accessing values by keys
        - Iterating over keys, values, and items
        - Checking membership
        - Retrieving keys, values, and items as iterable objects
    
    Dict is a class which is mutable, not hashable, and iterable
    it is not in sequesnce
    Dict can not have duplicate key
    Indexing is not applicable here (slicing operator is not applicable)
"""

class DictDemo:
    
    def __init__(self, elements=None):
        #Initialize dictionary with given elements or an empty dictionary.
        self.elements = elements if elements is not None else {}
    
    def display_dict(self):
        #Display dictionary elements.
        print("Dictionary Elements:", self.elements)
    
    def add_or_update(self, key, value):
        #Add a new key-value pair or update an existing key.
        self.elements[key] = value
        print(f"Added/Updated ({key}: {value}):", self.elements)
    
    def remove_key(self, key):
        #Remove a key-value pair if the key exists.
        if key in self.elements:
            del self.elements[key]
            # self.elements.pop(key)
            print(f"Removed key {key}:", self.elements)
        else:
            print(f"Key {key} not found in dictionary.")
    
    def get_value(self, key):
       #Retrieve a value by key.
        print(f"Value for key {key}:", self.elements.get(key, "Key not found"))
    
    def iterate_keys(self):
        #Iterate over dictionary keys.
        print("Keys:", list(self.elements.keys()))
        #keys() --> collection of keys only
    
    def iterate_values(self):
        #Iterate over dictionary values.
        print("Values:", list(self.elements.values()))
        #values() --> collection of the values only
    
    def iterate_items(self):
        #Iterate over dictionary key-value pairs.
        print("Items:")
        for key, value in self.elements.items():
            print(f"{key}: {value}")
        #items() --> collection dict elements;
    
    def check_membership(self, key):
        #Check if a key is present in the dictionary.
        print(f"Is {key} in dictionary?:", key in self.elements)
    
    def clear_dict(self):
        #Clear all elements from the dictionary.
        self.elements.clear()
        print("Dictionary cleared.")


# Demonstrating the DictDemo class
demo = DictDemo({"name": "Alice", "age": 25, "city": "New York"})
demo.display_dict()
demo.add_or_update("age", 26)
demo.add_or_update("country", "USA")
demo.remove_key("city")
demo.get_value("name")
demo.iterate_keys()
demo.iterate_values()
demo.iterate_items()
demo.check_membership("age")
demo.clear_dict()
