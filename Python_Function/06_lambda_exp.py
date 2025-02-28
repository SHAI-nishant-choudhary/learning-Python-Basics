# Define a class that demonstrates lambda expressions
class Calculator:
    def __init__(self):
        # Lambda expressions for basic arithmetic operations
        self.add = lambda a, b: a + b 
        # similar to 
        # def fun(a,b): 
        #   return a+b
        self.subtract = lambda a, b: a - b
        self.multiply = lambda a, b: a * b
        self.divide = lambda a, b: a / b if b != 0 else 'Undefined (division by zero)' 
        #similar to
        # def func(a,b):
        #   if b!=0:
        #       return a/b
        #   else :
        #       return "Undefined (division by zero)"
    
    def operate(self, operation, a, b):
        """
            Method to execute the given operation.
                :param operation: Function (lambda expression) to execute
                :param a: First operand
                :param b: Second operand
                :return: Result of the operation
        """
        return operation(a, b)

# Create an instance of Calculator
calc = Calculator()

# Demonstrating lambda expressions in action
print("Addition: ", calc.operate(calc.add, 10, 5))              # Output: 15
print("Subtraction: ", calc.operate(calc.subtract, 10, 5))      # Output: 5
print("Multiplication: ", calc.operate(calc.multiply, 10, 5))   # Output: 50
print("Division: ", calc.operate(calc.divide, 10, 5))           # Output: 2.0
