# A class to demonstrate recursion using Object-Oriented Programming (OOP) principles.
class RecursionDemo:
   
    def factorial(self, n):
        """
            Recursively calculates the factorial of a given number.
                :param n: Non-negative integer
                :return: Factorial of n
        """
        if n == 0 or n == 1:  # Base case
            return 1
        else:
            return n * self.factorial(n - 1)  # Recursive call

    def fibonacci(self, n):
        """
            Recursively calculates the nth Fibonacci number.
                :param n: Non-negative integer
                :return: nth Fibonacci number
        """
        if n == 0:  # Base case 1
            return 0
        elif n == 1:  # Base case 2
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)  # Recursive call

# Create an instance of the class
demo = RecursionDemo()

# Demonstrate factorial recursion
num = 5
print(f"Factorial of {num} is: {demo.factorial(num)}")

# Demonstrate Fibonacci recursion
fib_index = 6
print(f"Fibonacci number at index {fib_index} is: {demo.fibonacci(fib_index)}")

"""
    Explanation:
        Class RecursionDemo: Encapsulates the recursive functions.
            Method factorial(self, n):
                Base case: If n is 0 or 1, return 1.
                Recursive case: n * factorial(n - 1).
                #for factorial(5)
                        factorial(5)
                        |
                        ↓
                        5 * factorial(4)
                        |
                        ↓
                        4 * factorial(3)
                        |
                        ↓
                        3 * factorial(2)
                        |
                        ↓
                        2 * factorial(1)
                        |
                        ↓
                        1 (Base case)

                
            Method fibonacci(self, n):
                Base cases: F(0) = 0, F(1) = 1.
                Recursive case: F(n) = F(n-1) + F(n-2).
                #For fibbonacci(6)
                                    fib(6)
                                    /        \
                                fib(5)        fib(4)
                                /      \       /      \
                            fib(4)    fib(3)  fib(3)  fib(2)
                            /      \   /    \  /    \   /    \
                        fib(3)  fib(2) fib(2) fib(1) fib(2) fib(1) fib(0)
                        /    \   /    \   /    \
                    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
                    /    \
                fib(1) fib(0)

    Object Creation: An instance of RecursionDemo is created to invoke the methods.
    Demonstration: Calls the methods for sample inputs and prints the results.
"""
