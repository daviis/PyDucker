"""
All classes contained within are wrappers around instance data dealing with ast traversal

@author: Emily 2014/10/20
revised: Jake 2014/11/12
"""
import sys
import Exceptions 

class GenericBean():
    
    def __init__(self, name, initialize):
        """
        @name:str
        @initalize:bool
        """
        self.name = name
        self.initialize = initialize

class ClassDefBean(GenericBean):
    
    def __init__(self, classname, selfVars, rent = 'object'):
        """
        @className:str
        @selfVars:ScopeLevelBean
        @rent:str
        """
        self.name = classname
        self.varinfo = selfVars
        self.funs = {} #of key = Fundef.name, FunDefBean for faster look up
        self.parent = rent #the name of the parent varType
        
    def hasFun(self, op):
        """
        @op:str
        """
        return op in self.funs
    
    def acceptsFun(self, fun):
        """
        @fun:FunDefBean
        """
        try:
            if self.funs[fun.name] == fun:
                return self.funs[fun.name].returnType 
        except KeyError:
            raise Exceptions.MissingMethodException(self, fun.name)
        except Exceptions.IncorrectMethodExcepiton as ex:
            ex.cls = self
            raise ex
            
    def isIterable(self):
        if not "__iter__" in self.funs:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__iter__")

    def isCallable(self):
        if not "__call__" in self.funs:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__call__")
    
    def isString(self):
        if not "__str__" in self.funs:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__str__")
    
    def isBoolean(self):
        if not "__bool__" in self.funs:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__bool__")
            


class FunDefBean(GenericBean):
    
    def __init__(self, paramsTypes, returntype, fundefname):
        """
        @paramsTypes:*VarBean
        @returnType:VarBean
        @fundefname:str
        """
        self.partOfClass = False
        self.typesparams = paramsTypes
        self.returnType = returntype
        self.name = fundefname
        self.numparams = len(self.typesparams) # this should be assigned after creation to be length of self.typesparams

    def takes(self, paramList):
        """
        @paramList:str*
        todo:expand so it can also take optional vars and list/dicts
        """
        if not len(paramList) == len(self.typesparams):
            return False
        for idx in range(len(paramList)):
            if not paramList[idx].varType == self.typesparams[idx]:
                return False
        return True

    def __eq__(self, funBean):
        """
        @funBean:FunDefBean
        Like takes but uses a fundefbean instead of a string
        """
        if self.takes(funBean.typesparams):
            return True
        else:
            raise Exceptions.IncorrectMethodExcepiton(funBean.name, funBean.typesparams)

class VarBean(GenericBean):
    
    def __init__(self,  aType, aName = '_'):
        """
        This is what the varType of one variable should be. If it is a collection of subtypes them more of the fields come into play.
        These fields are homo and compType. Homo is a boolean to see if all of the subtypes are the same. If they are, then compType will
        be a list with only one str. Otherwise it will be a list with the initial types. 
        Neither of these fields should be accessed directly. Instead call nextSubType()
        
        Starred is a field to see if the var is supposed to be unpacked into. It might be set in visit_Starred and looked up in visit_ASssign. 
        @name:str
        @aType:str
        """
        self.name = aName
        self.varType = aType
        self.homo = False
        self.starred = False
        self.compType = []
        
    def __eq__(self, other):
        return self.varType == other
    
    def nextSubType(self):
        if self.homo:
            return self.compType[0].varType
        else:
            return self.compType
            
    def typesMatch(self, other):
        if self.compType:
            if self.homo:
                return self.compType[0] == other.compType[0] and self.varType == other.varType
            else:
                return self.varType == other.varType and  all(x == self.compType[0] for x in self.compType)
        else:
            if self.varType:
                return self.varType == other.varType
            else:
                return True #currently the value of self.varType == None 
            

class ScopeLevelBean(GenericBean):
    
    def __init__(self, incomingVars = []):
        """
        @incomingVars:*VarBean
        The key in the levels dictionary will be the varName, value will be the VarBeanReference
        """
        self.levels = [{}]
        for var in incomingVars:
            self.append(var)
        
        
    def __getitem__(self, item):
        """
        @item:str
        """
        currentLevel = self.levels.pop()
        self.levels.append(currentLevel)
        return currentLevel[item]
    
    def __setitem__(self, name, item):
        """
        Set a variable in the highest level of scope
        """
        currentLevel = self.levels.pop()
        currentLevel[name] = item
        self.levels.append(currentLevel)
        
    def __delitem__(self,item):
        """
        @item:str
        Delete an entry from scope where item is the key
        """
        currentLevel = self.levels.pop()
        del currentLevel[item]
        self.levels.append(currentLevel)
        
    def __contains__(self, item):
        """
        @item:str
        @!bool
        """
        currentLevel = self.levels.pop()
        self.levels.append(currentLevel)
        return item in currentLevel
        
    def __iter__(self):
        currentLevel = self.levels.pop()
        self.levels.append(currentLevel)
        return iter(currentLevel)
        
    def append(self, item):
        """
        @item:VarBean
        """
        currentLevel = self.levels.pop()
        
        if item.name in currentLevel and item != currentLevel[item.name]:
            print("reassign of " + item.name, file=sys.stderr)
            
        currentLevel[item.name] = item
        self.levels.append(currentLevel)
        
    def goDownLevel(self):
        """
        Used when entering a function, it adds a dictionary to the stack of scope levels
        """
        self.levels.append({})
    
    def goUpLevel(self):
        """
        Used when leaving a function, it pops a dictionary to the stack of scope levels
        """
        self.levels.pop()
        
        
        
class NameSpaceBean(GenericBean):
    """
    This variation of ScopeLevelBean will wrap a dictionary where the key will be a string of the class/fun name
    and the value will be a ClassBean or FunDefBean. The look up will be different because if it hits on a value 
    in the dict that is initialized with None then it will attempt to make a bean.
    """
    
    def __init__(self):
        self.vars = {}
     
    def put(self, name, bean=None):
        """
        @name:str
        @bean:GenericBean
        """
        self.vars[name] = bean
        
    def __getitem__(self,key):
        """
        An incomplete method only the bare minimum now.
        @key:str
        """
        if key in self.vars:
            if self.vars[key] == None:
                pass #make a bean here
            return self.vars[key]
        else:
            return None
        
    def checkCreate(self, clsName, args=None, kwargs=None):
        """
        @clsName:str
        @args:VarBean*
        @kwargs:str**
        """
        return self.vars[clsName].checkCreate(args, kwargs)
    
    def duckBool(self, varBean):
        """
        @varBean:VarBean
        Check to see if the class can be evaluated into a boolean, if not an exception is raised in ClassDefBean.
        """
        self.vars[varBean.varType].isBoolean()
        
    def duckStr(self, varBean):
        """
        @varBean:VarBean
        Same as duckbool
        """
        self.vars[varBean.varType].isString()
        
    def duckIter(self, varBean):
        """
        @varBean:VarBean
        """
        self.vars[varBean.varType].isIterable()
    
    def checkMagicMethod(self, lbean, rbean, op):
        """
        A method for visit_Binop and visit_AugAssign. It does exception raising and namespace checks.
        @lBean:VarBean
        @rBean:VarBean
        @op:str
        """
        rOp = op[:2] + 'r' + op[2:]
        fstFun = FunDefBean([rbean], None, op)
        sndFun = FunDefBean([lbean], None, rOp)
        
        #look up if the method is contained in the left, if not then maybe the right
        #if so, then return the return varType of the function
        #if not, raise missingMagicMethodException
        for bean, fun in ((lbean, fstFun), (rbean, sndFun)):
            try:
                resultType = self.vars[bean.varType].acceptsFun(fun)
                return resultType
            except Exceptions.MissingMethodException:
                pass
        raise Exceptions.MissingMagicMethodException(lbean, rbean, op, rOp)
            
