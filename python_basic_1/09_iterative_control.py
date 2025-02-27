# Iterative Control (while ,for)

#while
class Printer:
    """
    A class that contains a method to print 'Shorthills' five times.
    """
    
    def print_shorthills(self):
        """
        Prints 'Shorthills' five times using a while loop.
        """
        count = 0  # Initialize counter
        while count < 5:
            print("Shorthills")  # Print 'Shorthills'
            count += 1  # Increment counter

# Example usage
printer = Printer()  # Create an instance of Printer class
printer.print_shorthills()  # Call the method to print 'Shorthills'


#for loop
class Printer2:
    """
    A class that contains methods to demonstrate the usage of loops in Python.
    """
    
    def print_shorthills_while(self):
        """
        Prints 'Shorthills' five times using a while loop.
        """
        count = 0  # Initialize counter
        while count < 5:
            print("Shorthills")  # Print 'Shorthills'
            count += 1  # Increment counter
    
    def print_shorthills_for(self):
        """
        Prints 'Shorthills' five times using a for loop.
        """
        for _ in range(5):  # Loop runs 5 times
            print("Shorthills")  # Print 'Shorthills'

# Example usage
printer = Printer2()  # Create an instance of Printer class
printer.print_shorthills_while()  # Call the method using while loop
printer.print_shorthills_for()  # Call the method using for loop
