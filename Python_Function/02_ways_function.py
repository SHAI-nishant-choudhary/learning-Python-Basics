"""
There are 4 different ways to create a function
    1) take nothing return nothing
    2) take nothing return something
    3) take something return nothing
    4) take something return something
"""
class FunctionDemo:
    def take_nothing_return_nothing(self):
        #Method that takes nothing and returns nothing
        print("This method takes nothing and returns nothing.")
    
    def take_nothing_return_something(self):
        #Method that takes nothing but returns something
        return "This method takes nothing but returns a string."
    
    def take_something_return_nothing(self, name):
        #Method that takes something but returns nothing
        print(f"Hello, {name}! This method takes a name but returns nothing.")
    
    def take_something_return_something(self, a, b):
        #Method that takes something and returns something
        return a + b

# Creating an object of FunctionDemo class
demo = FunctionDemo()

# Calling methods
demo.take_nothing_return_nothing()

result = demo.take_nothing_return_something()
print("Returned Value:", result)

demo.take_something_return_nothing("Alice")

sum_result = demo.take_something_return_something(10, 20)
print("Sum Result:", sum_result)
