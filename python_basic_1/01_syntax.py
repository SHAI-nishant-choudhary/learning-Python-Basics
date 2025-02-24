#just for checking
print("Hello World") 
a = int(input("Enter a number "))
print("Value of a is",a)


#indentation is most crucial in python for ease of readability and for python syntax
# uneccasary indentation would leads to compile time error
"""
    if a>0:
    print(a)
        print(a*2)
    #error occur
"""

#proper indentation must required
if a > 0:
    print("Postive Number")
else :
    print("Non Postive Number")
    
for e in range(0,10):
    print("Value of e ",e)
    