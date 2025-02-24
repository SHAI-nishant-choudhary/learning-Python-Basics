""" 

varibale name conatains
i).alphabetic in small or captial
ii).numeric
iii) "_" underscore

if variable name contain other than this charcter it will give error
variable name should start with alphabetic character or underscore.
var name should be different from reserved keyword

"""


#how to check type of variable --> predefined "type()" function
class typeCheck:
    x=10
    def check(self):
         return type(self.x)
     
obj = typeCheck() # declare class object obj
print(obj.check()) #call class member function by using . operator


#Assign multiple values
class MultiVal:
    x, y, z = "Orange", "Banana", "Cherry"
    def show(self):
        print(self.x, self.y, self.z)

obj = MultiVal() #we can reassign the value or change the type of any variable any time 
obj.show()




#GLOBAL VARIABLE
#global variable: Global variables can be used by everyone, both inside of functions and outside.


x = "awesome"
class GlobalVar:
    #Creating a variable outside of a function, and use it inside the function
    def myfunc1():
        print("Python is " + x)
        
        
    #Creating a variable inside a function, with the same name as the global variable
    def myfunc2():
        x = "fantastic"
        print("Python is " + x)  #Output: Python is fantastic
    
obj  = GlobalVar();
obj.myfunc1() #Output: Python is awesome

obj.myfunc2() #Output: Python is fantastic
print("Python is " + x)  #Output: Python is awesome


