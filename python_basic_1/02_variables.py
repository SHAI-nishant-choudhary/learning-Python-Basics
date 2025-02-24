#Variables are containers for storing data values.
class PythonVariabes:
    x=1  #assigning int variable
    y=1.22 #assigning float variable
    z=3+4j  #assigning complex variable
    flag=True #assigning Boolen variable
    
    def intVar(self):
        print(self.x) #print int var on screen
        
    def floatVar(self):
        print(self.y) #print float var on screen
    
    def complexVar(self):
        print(self.z)   #print complex var on screen
        
    def boolVar(self):
        print(self.flag) #print boolean var on screen
        
    
var = PythonVariabes()
var.intVar() #cal intVar function which print int varibale 
var.floatVar() #cal floatVar function which print float varibale 
var.complexVar() #cal complexvar function which print complex varibale 
var.boolVar() #cal boolvar function which print bool varibale 

    