#check example
def func():
    print("Hello World")
a= func() # Output: Hello World
print(a) #Output : None

def func2():
    print("Hello World World")
a=func2
print(a,type(a),a()) 
# Output:  Hello World World
# <function func2 at 0x7740cb68d120> <class 'function'> None
#Note : a() is function call and it in call first or before print 





"""
    Different types of Argument
        1) Postional Argument
        2) Keyword Argument
        3) variable length argument (*args)
        4) variable keyword Argument (**kwargs)
"""
class Calculator:
    def __init__(self, a, b):
        """
            Constructor with positional arguments
                :param a: First number
                :param b: Second number
        """
        self.a = a
        self.b = b

    def add(self):
        #Method using positional arguments
        return self.a + self.b

    def subtract(self, x, y):
        #Method using positional arguments
        return x - y

    def multiply(self, x=1, y=1):
        #Method using keyword arguments with default values
        return x * y

    def divide(self, *args):
        #Method using variable-length positional arguments (*args)
        result = args[0]  # Take first element as initial result
        for num in args[1:]:
            if num == 0:
                return "Division by zero error"
            result /= num
        return result

    def show_details(self, **kwargs):
        #Method using variable-length keyword arguments (**kwargs)
        for key, value in kwargs.items():
            print(f"{key}: {value}")

# Creating object with positional arguments
calc = Calculator(10, 5)

# Using positional arguments
print("Addition:", calc.add())
print("Subtraction:", calc.subtract(20, 10))

# Using keyword arguments
print("Multiplication:", calc.multiply(y=4, x=3))

# Using variable-length positional arguments (*args)
print("Division:", calc.divide(100, 2, 5))

# Using variable-length keyword arguments (**kwargs)
calc.show_details(name="Advanced Calculator", version=1.0, author="ChatGPT")

"""
    NOTE: You cannot have positional arguments after keyword arguments.
    #Example
    def f1(a,b):
        print("a = ",a, "b = ",b)
    f1(2,3)     --> 2,3 are called positional arguments
    f1(b=2,a=3) --> this is keyword argument

    #f1(b=3,2)  --> throw an error

"""