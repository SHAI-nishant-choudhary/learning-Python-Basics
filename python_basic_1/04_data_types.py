"""

    Variables can store data of different types, and different types can do different things.
    Python has the following data types built-in by default, in these categories:
    
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
    
"""
class DataTypes:
    x = 1234 #int
    y = "Nishant Choudhary" #string
    l = [1,2,3,4] #list
    c = 3+4j  #complex
    flag = True #boolean
    
    def show(self):
        #print all variables
        print(self.x, self.y, self.l, self.c, self.flag)
        #print variable's data types
        print(type(self.x),type(self.y),type(self.l),type(self.c),type(self.flag))
        
    
obj = DataTypes()
obj.show()
    
    