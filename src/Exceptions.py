'''
Created on Dec 4, 2014

@author: daviis01

The exception hierarchy for PyDucker is 

|---PyDuckerException
    |--- PyDuckerError
         |--- MissingMethodException
              |--- MissingMagicMethodException
              |--- IncorrectMethodException
    |--- PyDuckerWarning
         |--- TypeMissmatchException
'''
from Bean import ClassDefBean 

class PyDuckerException(Exception):
    def __init__(self, lineNo):
        """
        @lineNo:int
        """
        self.lineNum = lineNo
        
    def __str__(self):
        return "\n\tOn line: " + str(self.lineNum)
    
    
class PyDuckerError(PyDuckerException):
    def __init__(self, lineNo):
        """
        @lineNo:int
        """
        super().__init__(lineNo)
        
class PyDuckerWarning(PyDuckerException):
    def __init__(self, lineNo):
        """
        @lineNo:int
        """
        super().__init__(lineNo)
        
        

class TypeMissMatchException(PyDuckerWarning):
    
    def __init__(self, var, old, new, lineNu):
        """
        @var:str
        @old:str
        @new:str
        @lineNu:int
        """
        super().__init__(lineNu)
        self.varName = var
        self.oldType = old
        self.newType = new
    
    def __str__(self):
        ret = super().__str__()
        ret += "\nVar name : " + self.varName + "\n\told type: " + self.oldType + "\tnew type: " + self.newType + "\n\tline number: " + str(self.lineNum)
        return ret
    
    
    
class MissingMethodException(PyDuckerError):
    
    def __init__(self, aCls, aFun, lineNo):
        """
        @aCls:ClassDefBean
        @aFun:str
        @lineNu:int
        """
        super().__init__(lineNo)
        self.cls = aCls
        self.fun = aFun
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCan not find method: " + self.fun
        ret += "\n\tIn class: " + self.cls.name
        return ret
    
    
    
class MissingMagicMethodException(MissingMethodException):
    
    def __init__(self, leftOne, rightOne, aOp, aRop, lineNo):
        """
        @left:ClassDefBean
        @right:ClassDefBean
        @op:str
        @rop:str
        @lineNu:int
        """
        super().__init__(leftOne, aOp, lineNo)
        self.cls2 = rightOne
        self.rop = aRop
        
    def __str__(self):
        ret = super().__str__()
        ret += " that takes: " + self.cls2.name
        ret += "\n\tOr can not find method: " + self.rop + " \n\tIn class: " + self.cls2.name + " that takes: " + self.cls.name 
        return ret
    
    
    
class IncorrectMethodExcepiton(MissingMethodException):
    
    def __init__(self, aCls, aFun, someArgs, lineNo):
        """
        @aCls:ClassDefBean
        @aFun:str
        @someArgs:^str
        @lineNo:int
        """
        super().__init__(aCls, aFun, lineNo)
        self.argLst = someArgs
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tWith args: " + str(self.argLst)
        return ret