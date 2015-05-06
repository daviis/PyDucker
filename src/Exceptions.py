'''
Created on Dec 4, 2014

@author: daviis01

The exception hierarchy for PyDucker is 

|---PyDuckerException
    |--- PyDuckerError
         |--- MissingMethodException
              |--- MissingMagicMethodException
              |--- IncorrectMethodException
              |--- IncorrectMethodKeywordException
        |--- OutOfScopeException
             |--- RefBeforeAssignException 
        |--- MissingDocStringException
        |--- NonlocalReferenceException
        |--- GlobalReferenceException
        |--- PyDuckerSyntaxError
        |--- DataMemberDecOutsideInit
    |--- PyDuckerWarning
         |--- TypeMismatchException
         |--- HeteroCollecionException
         |--- ScopeNotFoundException
         |--- KeyWordFromAVariable
         |--- MultiReturnTypeException
         
'''

class PyDuckerException(Exception):
    def __init__(self, lineNo):
        """
        @lineNo:int
        """
        self.lineNum = lineNo
        
    def __str__(self):
        return "\n\tOn line: " + str(self.lineNum)
    
    
class PyDuckerError(PyDuckerException):
    def __init__(self, lineNo=-1):
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
        
        

class TypeMisMatchException(PyDuckerWarning):
    
    def __init__(self, var, old, new, lineNu):
        """
        @var:str
        @old:VarBean
        @new:VarBean
        @lineNu:int
        """
        super().__init__(lineNu)
        self.varName = var
        self.oldType = old
        self.newType = new
    
    def __str__(self):
        ret = super().__str__()
        print("\n\tVar name : " + self.varName + "\n\told type: " + self.oldType.varType + "\n\new type: " + self.newType.varType)
        ret += "\n\tVar name : " + self.varName + "\n\told type: " + self.oldType.varType + "\n\new type: " + self.newType.varType
        
        return ret
    
    
class HeteroCollecionException(PyDuckerWarning):
    
    def __init__(self, var, lineNu=-1):
        """
        @var:str
        @lineNu:int
        """
        super().__init__(lineNu)
        self.varName = var
        
    def __str__(self):
        ret = super().__str__()
        ret += "\nVaribale: " + self.varName + " is a heterogeneous collection"
        return ret
    

class OutOfScopeException(PyDuckerError):
    
    def __init__(self, someName, lineNo=-1):
        """
        @someName:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.aName = someName
        self.extraMessage = ""
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tVariable name: " + self.aName + " is not in scope"
        ret += "\n\t" + self.extraMessage
        return ret
    
class RefBeforeAssignException(OutOfScopeException):
    
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tBecause it was referenced before it was assigned."
        return ret
    
class MissingDocStringException(PyDuckerError):
    

    def __init__(self, someName, lineNo=-1):
        """
        @someName:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.aName = someName
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tVarible name: " + self.aName + " in a DocString"
        return ret
    
class MissingMethodException(PyDuckerError):
    
    def __init__(self, aVar, aFun, lineNo=-1):
        """
        @aCls:VarBean
        @aFun:str
        @lineNu:int
        """
        super().__init__(lineNo)
        self.cls = aVar
        self.fun = aFun
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCan not find method: " + self.fun
        ret += "\n\tIn class: " + self.cls.varType
        return ret
    
    
    
class MissingMagicMethodException(MissingMethodException):
    
    def __init__(self, leftOne, rightOne, aOp, aRop, lineNo=-1):
        """
        @left:VarBean
        @right:VarBean
        @op:str
        @rop:str
        @lineNu:int
        """
        super().__init__(leftOne, aOp, lineNo)
        self.cls2 = rightOne
        self.rop = aRop
        
    def __str__(self):
        ret = super().__str__()
        ret += " that takes: " + self.cls2.varType
        ret += "\n\tOr can not find method: " + self.rop + " \n\tIn class: " + self.cls2.varType + " that takes: " + self.cls.varType 
        return ret
    
    
    
class IncorrectMethodException(MissingMethodException):
    
    def __init__(self, aFun, someArgs, lineNo=-1, aCls=None, kws={}, star=None):
        """
        @aCls:VarBean
        @aFun:str
        @someArgs:^VarBean
        @lineNo:int
        @kws:str**VarBean
        @star:VarBean
        """
        super().__init__(aCls, aFun, lineNo)
        self.argLst = someArgs
        self.kwargs = kws
        self.starargs = star
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tWith args:"
        for item in self.argLst:
            ret += " " + item.varType + ","
        if self.starargs:
            ret += "\n\tAnd starred args:" 
            for comp in self.starargs.compType:
                ret += " " + comp.varType
        for key in self.kwargs:
            ret += "\n\tAnd keyword args: '" + key + "' = " + self.kwargs[key].varType + ","
        return ret
    
    
class IncorrectMethodKeywordException(MissingMethodException):
    
    def __init__(self, missingKeyword, aFun=None, aCls = None, lineNo=-1):
        """
        @missingKeyword:VarBean
        """
        super().__init__(aCls, aFun, lineNo)
        self.keyword = missingKeyword
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tWith keyword: " + self.keyword.name
        ret += "\n\tOf type: " + self.keyword.varType
        return ret
    
class NonlocalReferenceException(PyDuckerError):
    
    def __init__(self, aVarBeanLst, message, lineNo=-1):
        """
        @aVarBeanLst:VarBean*
        @message:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.msg = message
        self.varBeanList = aVarBeanLst
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCouldn't make nonlocal call about "
        for bean in self.varBeanList:
            ret += bean.name
        ret += "\n\t" + self.msg
        return ret
    
class GlobalReferenceException(PyDuckerError):
    
    def __init__(self, nameBean, message, lineNo=-1):
        """
        @nameBean:VarBean
        @message:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.msg = message
        self.varBean = nameBean
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCouldn't make global call for " + self.varBean.name
        ret += "\n\t" + self.msg
        return ret
    
class PyDuckerSyntaxError(PyDuckerError):
    
    def __init__(self, message, lineNo=-1):
        """
        @message:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.msg = message
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\t" + self.msg
        return ret
    
    
class ScopeNotFoundException(PyDuckerWarning):
    
    def __init__(self, globNonLoc, aVarBean, lineNo=-1):
        """
        @globNonLoc:str
        @aVarBean:Bean.VarBean
        @lineNo:int
        """
        super().__init__(lineNo)
        self.varBean = aVarBean
        self.scopeType = globNonLoc
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tCould not find " + self.varBean.name + " in the scope of " + self.scopeType
        return ret
    
class KeyWordFromAVariable(PyDuckerWarning):
    
    def __init__(self, aVar, lineNo=-1):
        """
        @aVar:Bean.VarBean
        @lineNo:int
        """
        super().__init__(lineNo)
        self.varBean = aVar
         
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tUnable to check to see if a keyword is acceptable when read out of a variable."
        ret += "\n\tThe variable found was: " + self.varBean.name
        return ret
    
class MultiReturnTypeException(PyDuckerWarning):
    
    def __init__(self, anOldType, aNewType, lineNo=-1):
        """
        @anOldType:Bean.VarBean
        @aNewType:Bean.VarBean
        @lineNo:int
        """
        super().__init__(lineNo)
        self.oldType = anOldType
        self.newType = aNewType
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tOld type: " + self.oldType.varType
        ret += "\n\tNew type: " + self.newType.varType
        return ret

class DataMemberDecOutsideInit(PyDuckerError):
    
    def __init__(self, funName, varName, lineNo=-1):
        """
        @funName:str
        @varName:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.fun = funName
        self.var = varName
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tData members are only allowed to be declaired in the __init__ function to be typed by pyducker"
        ret += "\n\tFunction Name: " + self.fun
        ret += "\n\tVariable Name: " + self.var
        return ret

class NonIndexableException(PyDuckerError):
    
    def __init__(self, varBean, dictBean, lineNo=-1):
        """
        @varBean:str
        @lineNo:int
        """
        super().__init__(lineNo)
        self.varBean = varBean
        
    def __str__(self):
        ret = super().__str__()
        ret += "\n\tVariable name: " + self.varBean.name + " is an " + self.varBean.varType +" and needs to be a key or value for " + self.dictBean.name + " in order to index."
        return ret
