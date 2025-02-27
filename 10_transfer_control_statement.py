
"""
 Transfer Control Statement
 1) break
 2) continue
"""
"""
break and continue is a keyword
break is used to tranfer control outside the loop body
Continue can only be used in the body loop it continue the transfer the control immedeatly to the next iteration

"""

class Printer:
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
    
    def demonstrate_break(self):
        """
        Demonstrates the use of 'break' in a for loop.
        The loop stops when i reaches 3.
        """
        for i in range(5):
            if i == 3:
                break  # Exit loop when i reaches 3
            print(f"Break Example: {i}")  # Print the current value of i
    
    def demonstrate_continue(self):
        """
        Demonstrates the use of 'continue' in a for loop.
        The loop skips printing when i equals 2.
        """
        for i in range(5):
            if i == 2:
                continue  # Skip the current iteration when i is 2
            print(f"Continue Example: {i}")  # Print the current value of i

# Example usage
printer = Printer()  # Create an instance of Printer class
printer.print_shorthills_while()  # Call the method using while loop
printer.print_shorthills_for()  # Call the method using for loop
printer.demonstrate_break()  # Call the method demonstrating 'break'
printer.demonstrate_continue()  # Call the method demonstrating 'continue'
