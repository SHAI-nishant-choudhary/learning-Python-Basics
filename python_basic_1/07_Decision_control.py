"""
    There are 3 types of control statement
    1) Decision control
    2) Match case
    3) Iterative control
"""

#Decision Control ( if,if else, if elif else, single line if else)

#if
class CheckPositive:
    def __init__(self,a): #constructor run at first when class object created
        self.a=a        #initialisze class variable with outside variable
    
    def checkPos(self): #self means reference of object call it
        if self.a>0:    #if condtion is true then its block run
            print("Positive Number") 
        if self.a<=0:
            print("Non Positive")
    
num= int(input("Enter a number:"))
obj=CheckPositive(num)
obj.checkPos() #object calling member function


#if else
class CheckPositive2:
    def __init__(self,a): #constructor run at first when class object created
        self.a=a        #initialisze class variable with outside variable
    
    def checkPos(self): #self means reference of object call it
        if self.a>0:    #if condtion is true then its block run and if condition is false then else block will run
            print("Positive Number") 
        else:
            print("Non Positive")

obj = CheckPositive2(num)
obj.checkPos()


#if elif else
class Result:
    def __init__(self,marks):
        self.marks=marks

    def printResult(self): # if elif else used when nesteing of if else occure repteadly
        if self.marks <=100 and self.marks >90:
            print("A")
        elif self.marks <=90 and self.marks >80:
            print("B")
        elif self.marks <=80 and self.marks >70:
            print("C")
        elif self.marks <=70 and self.marks >60:
            print("D")
        else:
            print("Fail")

obj = Result(num)
obj.printResult()


#single line if else
x=int(input("Enter a number"))
print("positive") if x>0 else print("Non Positive")
#single line if else is an expression 
#but if else is not an expression
x= x*2 if x<0 else x**2

