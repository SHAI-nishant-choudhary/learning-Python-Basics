"""
    Match statement is used to form a menu driven software
"""

class NumberCheck:
    def __init__(self,num):
        self.num=num
    def check(self): # case constant can be of any type
     #match and case are soft keywords this can be used as a varibale name
        match self.num:
            case 1:
                print("1")
            case 2:
                print("2")
            case 3:
                print("3")
            case _:
                print("Default number")

"""
    duplicate case is not an error but first match will only work
"""           

obj = NumberCheck(2)
obj.check() # output: 2