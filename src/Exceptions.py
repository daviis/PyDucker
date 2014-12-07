'''
Created on Dec 4, 2014

@author: daviis01
'''
class PyDuckerException(Exception):
    def __init__(self, lineNo):
        """
        @lineNo:int
        """
        self.lineNum = lineNo
        
    def __str__(self):
        return "\n\tOn line: " + str(self.lineNum)

class TypeMissMatchException(PyDuckerException):
    
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
    
class MissingMagicMethodException(PyDuckerException):
    
    def __init__(self, leftOne, rightOne, aOp, aRop, lineNo):
        """
        @left:str
        @right:str
        @op:str
        @rop:str
        @lineNu:int
        """
        super().__init__(lineNo)
        self.left = leftOne
        self.right = rightOne
        self.op = aOp
        self.rop = aRop
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCan not find magic method: " + self.op + " in class: " + self.left + " that takes: " + self.right + \
             "\n\tOr can not find magic method: " + self.rop + " in class: " + self.right + " that takes: " + self.left 
        return ret
    
class MissingMethodException(PyDuckerException):
    
    def __init__(self, aCls, aFun, lineNo):
        """
        @aCls:str
        @aFun:str
        @lineNu:int
        """
        super().__init__(lineNo)
        self.cls = aCls
        self.fun = aFun
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCan not find method: " + self.fun
        ret += "\n\tIn class: " + self.cls
        return ret
    
class IncorrectMethodExcepiton(MissingMethodException):
    
    def __init__(self, aCls, aFun, someArgs, lineNo):
        """
        @aCls:str
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