'''
Created on Dec 4, 2014

@author: daviis01
'''

class PyDuckerException(Exception):
    pass

class TypeMissMatchException(PyDuckerException):
    
    def __init__(self, var, old, new, lineNu):
        """
        @var:str
        @old:str
        @new:str
        @lineNu:int
        """
        self.varName = var
        self.oldType = old
        self.newType = new
        self.lineNum = lineNu
    
    def __str__(self):
        ret = "\nVar name : " + self.varName + "\n\told type: " + self.oldType + "\tnew type: " + self.newType + "\n\tline number: " + str(self.lineNum)
        return ret
    
class MissingMethodException(PyDuckerException):
    
    def __init__(self, leftOne, rightOne, aOp, aRop):
        """
        @left:str
        @right:str
        @op:str
        @rop:str
        """
        self.left = leftOne
        self.right = rightOne
        self.op = aOp
        self.rop = aRop
        
    def __str__(self):
        ret = "\n\tCan not find magic method: " + self.op + " in class: " + self.left + " that takes: " + self.right + \
             "\n\tOr can not find magic method: " + self.rop + " in class: " + self.right + " that takes: " + self.left 
        return ret