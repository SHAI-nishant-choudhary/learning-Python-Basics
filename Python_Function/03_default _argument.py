"""
Default Argument
    Dafault value indicates that the function argument will take that value if no argument value is
    passed during the function call.
    The default value is assigned by using the assignment "=" operator
        def func(a,b,c=0)

"""

# Defines a class named Greeter to encapsulate greeting functionality.
class Greeter:
    # Constructor method that initializes name and message with default values.
    def __init__(self, name="Guest", message="Welcome!"):
        self.name = name
        self.message = message
    
    # Defines a method to print a greeting message using the instance attributes.
    def greet(self):
        print(f"Hello, {self.name}! {self.message}")

# Creating objects with different parameters
# Creates an instance of Greeter with default values.
default_greeter = Greeter()
default_greeter.greet()

# Creates an instance of Greeter with a custom name but the default message.
alice_greeter = Greeter("Alice")
alice_greeter.greet()

# Creates an instance of Greeter with custom values for both parameters.
bob_greeter = Greeter("Bob", "Good to see you!")
bob_greeter.greet()
