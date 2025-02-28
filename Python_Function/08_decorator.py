"""
    #What is Decorator in Python
        A decorator in Python is a function that modifies the behavior of another function 
        or class method without changing its actual code. Decorators are widely used in Python 
        for logging, authentication, timing, and more.

    #How Decorator Work?
        Decorators take a function as input, add some functionality, and return a new function. 
        They are usually implemented using higher-order functions and closures.

"""

#example 1
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()  # Calling the original function
    return wrapper_function  # Returning the modified function

@decorator_function  #Applying the decorator
def say_hello():
    print("Hello!")

say_hello()

"""
Output:
    Wrapper executed before say_hello
    Hello!

"""


#Example 2

class ResultShow:
    def __init__(self, marks):
        self.marks = marks  # Store marks as an instance variable
    
    # Decorator function to check for distinction
    def deco_result(result):
        def distinction(self):
            for m in self.marks:
                if m >= 75:
                    print(m, "Good")  # Print "Good" for marks 75 and above
            else:
                result(self)  # Call the original result function
        return distinction

    @deco_result   # Applying the decorator to modify the result method
    def result(self):
        for m in self.marks:
            if m >= 33:
                pass  # Do nothing if mark is passing
            else:
                print("Fail")  # If any mark is below 33, print "Fail" and stop
                break
        else:
            print("Pass")  # If no failing marks, print "Pass"

# Sample marks list
l = [45, 78, 90, 63, 54]
obj = ResultShow(l)
obj.result()  # Call result method, which is decorated with distinction logic

"""
Output:
    78 Good
    90 Good
    Pass
"""