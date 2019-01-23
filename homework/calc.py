###'calc.py' module
###
### contains 'Calculator' class that emulates a simple calculator capable of
### addition, subraction, multiplication, division, and clearing the state (reset to 0)
###
### contains methods for aforementioned operations: add(),sub(),mul(),div(), & clr()
### as well as a result() function to actually return the value when desired


class Calculator:
    '''
    This class emulates a simple calculator capable of addition, subtraction, multiplication, division and clearing.
    
    It contains individual methods for doing the aforementioned operations.
    '''
    
    def __init__(self,number=0):
        '''
        Initiates the instance/object.
        
        Initiated to zero by default.
        '''
        self.number = number
        
    
    def add(self,num=0):
        '''
        Adds the given number to self.number.
        
        Adds zero by default
        '''
        self.number += num
    
    def sub(self,num=0):
        '''Subtracts the given number from self.number.
        
        Subtracts zero by default.
        '''
        self.number -= num
    
    def mul(self,num=1):
        '''
        Multiplies the given number by self.number.
        
        Multiplies by one by default.
        '''
        self.number *= num
    
    def div(self,num=1):
        '''Divides self.number by the given number.
        
        Divides by one by default.
        '''
        self.number /= num
    
    def clr(self):
        '''
        Resets/clears the self.number to zero.
        '''
        self.number = 0
    
    def result(self):
        '''
        Returns the self.number.
        '''
        return self.number
    
    

    
###if __name__ == "__main__":
 ###   import sys
  ###  fib(int(sys.argv[1]))