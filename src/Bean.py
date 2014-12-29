"""
All classes contained within are wrappers around instance data dealing with ast traversal

@author: Emily 2014/10/20
revised: Jake 2014/11/12
"""
import sys

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
        self.parent = rent #the name of the parent type
        
    def hasFun(self, op):
        """
        @op:str
        """
        return op in self.funs
    
    def isIterable(self):
        return "__iter__" in self.funs
    
    def isCallable(self):
        return "__call__" in self.funs
    
    def isBoolean(self):
        return "__bool__" in self.funs


class FunDefBean(GenericBean):
    
    def __init__(self, paramsTypes, returntype, fundefname):
        """
        @paramsTypes:*str
        @returnType:str
        @fundefname:str
        """
        self.partOfClass = False
        self.typesparams = paramsTypes
        if paramsTypes[0] == 'self':
            self.partOfClass = True
            self.typesparams = paramsTypes[1:]
        self.returnType = VarBean(returntype)
        self.name = fundefname
        self.numparams = len(self.typesparams) # this should be assigned after creation to be length of self.typesparams

    def takes(self, paramList):
        """
        @paramList:str*
        """
        if not len(paramList) == len(self.typesparams):
            return False
        for idx in range(len(paramList)):
            if not paramList[idx].type == self.typesparams[idx]:
                return False
        return True

class VarBean(GenericBean):
    
    def __init__(self,  aType, aName = '_'):
        """
        This is what the type of one variable should be. If it is a collection of subtypes them more of the fields come into play.
        These fields are homo and compType. Homo is a boolean to see if all of the subtypes are the same. If they are, then compType will
        be a list with only one str. Otherwise it will be a list with the initial types. 
        Neither of these fields should be accessed directly. Instead call nextSubType()
        @name:str
        @aType:str
        """
        self.name = aName
        self.type = aType
        self.homo = False
        self.compType = []
        
    def __eq__(self, other):
        return self.type == other.type
    
    def nextSubType(self):
        if self.homo:
            return self.compType[0].type
        else:
            return self.compType
            
    def typesMatch(self, other):
        if self.compType:
            if self.homo:
                return self.compType[0] == other.compType[0] and self.type == other.type
            else:
                return self.type == other.type and  all(x == self.compType[0] for x in self.compType)
        else:
            if self.type:
                return self.type == other.type
            else:
                return True #currently the value of self.type == None 
    


class ScopeLevelBean(GenericBean):
    
    def __init__(self, incomingVars = []):
        """
        @incomingVars:*VarBean
        """
        self.vars = {} #key will be the varName, value will be the VarBeanReference 
        for var in incomingVars:
            self.append(var)
        
    def __getitem__(self, item):
        """
        @item:str
        """
        return self.vars[item]
    
    def __setitem__(self, name, item):
        self.vars[name] = item
    
    def __contains__(self, item):
        """
        @item:str
        @!bool
        """
        return item in self.vars
        
    def __iter__(self):
        return iter(self.vars)
        
    def append(self, item):
        """
        @item:VarBean
        """
        if(item.name in self.vars):
            print("reassign of " + item.name, file=sys.stderr)
        self.vars[item.name] = item
        
    def copy(self):
        """
        Used to pass into a (class/fun)defWalker. When exited from the router it will pop off extra vars. 
        """
        bean = ScopeLevelBean()
        for varName in self.vars:
            bean.append(self.vars[varName])
        return bean
        
        
        
class NameSpaceBean(ScopeLevelBean):
    """
    This variation of ScopeLevelBean will wrap a dictionary where the key will be a string of the class/fun name
    and the value will be a ClassBean or FunDefBean. The look up will be different because if it hits on a value 
    in the dict that is initialized with None then it will attempt to make a bean.
    """
     
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
        