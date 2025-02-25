"""
    Python math Module
    Python has a built-in module that you can use for mathematical tasks.
    The math module has a set of methods and constants.
"""

#Math Module function
#Math Module Value
import math

class mathModule:
    x=math.e #Returns Euler's number (2.7182...)
    y=math.inf #Returns a floating-point positive infinity
    z=math.nan #Returns a floating-point NaN (Not a Number) value
    p=math.pi #Returns PI (3.1415...)
    
    
    def exponentialFunc():
        # Return the value of exponetenial power of different numbers
        print(math.exp(65)) # e^65
        print(math.exp(-9)) # e^-9
    
    def floorFunc():
        # Return the floor value of val
        print(math.floor(0.6)) # 0
        print(math.floor(-5.3)) # -6
        
    def ceilFunc():
        # Return the ceiling value of val
        print(math.ceil(5.3))
        print(math.ceil(-9.8))
        
    def gretestCommonDivisor():
        # Return the gretest common divisor of a and b
        print(math.gcd(5,15)) # 5
        print(math.gcd(-12,-36)) #12
        
    def squareRoot():
        # Return the square root of different numbers
        # Return A float value, representing the value of x to the power of 0.5 (x^0.5)
        print(math.sqrt(9))
        print(math.sqrt(2))
    
    def powerVal():
        # Returns the value of x raised to power y.
        # Return a float value, representing the value of x to the power of y (x^y)
        print(math.pow(9,3))
        print(math.pow(12,-2))
        