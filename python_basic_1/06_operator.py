"""
Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""


#Arithemetic Operators (+,-,*,/,%,**,//)
class arithmeticOperator:
    #Arithmetic operators are used with numeric values to perform common mathematical operations:
    a=15
    b=3
    def addition(self):
        #return addition of 2 operand
        print(self.a,self.b)
        
    def subtraction(self):
        #return subtraction of 2 operand
        print(self.a-self.b)
        
    def multiplication(self):
        #return multiplication of 2 operand
        print(self.a*self.b)
        
    def division(self):
        #return division of 2 operand
        print(self.a/self.b)
        
    def modulus(self):
        #return modulus or remeinder of 2 operand
        print(self.a%self.b)
        
    def exponentiation(self):
        #return x raise to the power y
        print(self.x**self.y)
    
    def floorDivision(self):
        #return floor division
        print(self.a//self.b)
        
obj=arithmeticOperator();
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
obj.modulus()
obj.exponentiation()
obj.floorDivision()
        
    
#Assignment Operators (=,+=,-=,/=,%=,//=,**=,&=,|=,^=,>>=,<<=,)
class assignmentOperator:
    #Assignment operators are used to assign values to variables
    a=15
    b=3
    def func(self):
        # print(a=b)
        self.a+=self.b #a=a+b
        print(self.a)
        self.a-=self.b #a=a-b
        print(self.a)
        self.a/=self.b #a=a/b
        print(self.a)
        self.a%=self.b #a=a%b
        print(self.a)
        self.a//=self.b #a=a//b
        print(self.a)
        self.a**=self.b #a=a**b
        print(self.a)
        self.a&=self.b #a=a&b
        print(self.a)
        self.a|=self.b #a=a|b
        print(self.a)
        self.a^=self.b #a=a^b
        print(self.a)
        self.a>>=self.b #a=a>>b
        print(self.a)
        self.a<<=self.b #a=a<<b
        print(self.a)

obj=assignmentOperator()
obj.func()


#Comparison Operators (==,!=,>,<,>=,<=)
class comparisonOperators():
    #Comparison operators are used to compare two values
    a=100
    b=101
    
    def equalTo(self):
        print(2==2.0)
        print(self.a==self.b)
    
    def notEqualTo(self):
        print(2==2.0)
        print(self.a==self.b)
    
    def greaterThan(self):
        print(2>2.0)
        print(self.a>self.b)
    
    def lessThan(self):
        print(2<2.0)
        print(self.a<self.b)
    
    def greaterThanOrEqualTo(self):
        print(2>=2.0)
        print(self.a>=self.b)
    
    def lessThanOrEqualTo(self):
        print(2<=2.0)
        print(self.a<=self.b)
        
obj=comparisonOperators()
obj.equalTo()
obj.notEqualTo()
obj.greaterThan()
obj.lessThan()
obj.greaterThanOrEqualTo()
obj.lessThanOrEqualTo()
    
       
#Logical Operators (and, or, not)
class logicalOperator:
    #Logical operators are used to combine conditional statements.
    
    def andOperator():
        #Returns True if both statements are true
        x=13
        print(x < 5 and  x < 10)
    
    def orOperator():
        #Returns True if one of the statements is true
        x=15
        print(x < 5 or x < 4)
        
    def notOperator():
        #Reverse the result, returns False if the result is true
        x=17
        print(not(x < 5 and x < 10))
    
obj=logicalOperator()
obj.andOperator()
obj.orOperator()
obj.notOperator()


#Identity Operators (is,is not)
class identityOperator:
    #Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
    def isOperator():
        x=9
        y=9
        print(x is y) #Returns True if both variables are the same object
    
    def isnotOperator():
        x=10
        y=10
        print(x is not y) #Returns True if both variables are not the same object
   
obj = identityOperator()
obj.isOperator()
obj.isnotOperator()


#Membership Operator(in,not in)
class membershipOperator:
    #Membership operators are used to test if a sequence is presented in an object
    def inOperator():
        l=[1,2,3,4,5]
        y=4
        print(y in l)
        #Returns True if a sequence with the specified value is present in the object
    
    def notinOperator():
        l = [1,2,3,4,5]
        z= 10
        print(z not in l)
        #Returns True if a sequence with the specified value is not present in the object

obj=membershipOperator()
obj.inOperator()
obj.notinOperator()


#Bitwise Opertaor (&,|,^,~,<<,>>)
class bitwiseOperator:
    #Bitwise operators are used to compare (binary) numbers
    x=8
    y=2
    
    def func(self):
        print(self.x & self.y) #sets each bit to 1 if both bits are 1
        print(self.x | self.y) #sets each bit to 1 if one of two bits is 1
        print(self.x ^ self.y) #Sets each bit to 1 if only one of two bits is 1
        print(~self.x) #Inverts all the bits
        print(self.x << 2) #Shift left by pushing zeros in from the right and let the leftmost bits fall off
        print(self.x >> 2) #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
        
obj = bitwiseOperator()
obj.func()



""" 
    Operator Precedence
    Operator precedence describes the order in which operations are performed.
    
        i).     Parentheses	
        ii).    Exponentiation	
        iii).   Unary plus, unary minus, and bitwise NOT	
        iv).    Multiplication, division, floor division, and modulus	
        v).     Addition and subtraction	
        vi).    Bitwise left and right shifts	
        vii).   Bitwise AND	
        viii).  Bitwise XOR	
        ix).    Bitwise OR	
        x).     Comparisons, identity, and membership operators	
        xi).    Logical NOT	
        xii).   AND	
        xiii).  OR
        
        If two operators have the same precedence, the expression is evaluated from left to right.

"""    



        