"""
    Higher Order Function
        Function which takes functions as a parameter and return a function
            1)map()
            2)reduce()
            3)filter()

        #Map
            map(function refrence , iterable objects)
            #example 
                def square(a):
                    return a**2
                x=map(square,[1,2,3,4])
                print(list(x),type(x)) #Output : (1,4,9,16) <map object>
                #x is map object

        #filter
            filter(function ref,iterable object)
            It is used to generate an output list of values that return true when the function is called
            #example
                def even(x):
                    if x%2==0:
                        return x
                y=filter(even,[5,3,2,5,0,4,8])
                print(list(y),type(y)) #Output: [2,0,4,8]
        
        #reduce
            reduce(function ref, iterable object)
            Function which applies a provided function to iterables and return a single value.

            from functool import reduce
            x=reduce(lambda a,b:a+b, [1,2,3,4])
            print(x) #Output : 10 -->(1+2+3+4)
            
"""

from functools import reduce

class DataProcessor:
    def __init__(self, data):
        """
            Constructor to initialize the list of numbers.
            param data: List of integers
        """
        self.data = data

    def apply_map(self, function):
        """
            Applies a given function to all elements using the map function.
                :param function: Function to apply to each element
                :return: List of transformed elements
        """
        return list(map(function, self.data))

    def apply_filter(self, function):
        """
            Filters elements based on a given function using the filter function.
                :param function: Function to filter elements
                :return: Filtered list of elements
        """
        return list(filter(function, self.data))

    def apply_reduce(self, function):
        """
            Reduces the list to a single value using the reduce function.
                :param function: Function to apply for reduction
                :return: Reduced single value
        """
        return reduce(function, self.data)

# Sample function to be used with map (square each number)
def square(n):
    return n * n

# Sample function to be used with filter (filter even numbers)
def is_even(n):
    return n % 2 == 0

# Sample function to be used with reduce (sum all elements)
def sum_numbers(x, y):
    return x + y

# Creating an instance of DataProcessor
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processor = DataProcessor(numbers)

# Applying map
mapped_result = processor.apply_map(square)
print("Mapped Result (Squares):", mapped_result)

# Applying filter
filtered_result = processor.apply_filter(is_even)
print("Filtered Result (Even Numbers):", filtered_result)

# Applying reduce
reduced_result = processor.apply_reduce(sum_numbers)
print("Reduced Result (Sum):", reduced_result)
