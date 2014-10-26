"""
All classes contained within are wrappers around instance data dealing with ast traversal

@author: Emily 2014/10/20
revised: Isaac 2014/10/22
"""
import sys

class GenericBean():
    
    def __inti__(self, name, initialize):
        """
        @name:str
        @initalize:bool
        """
        self.name = name
        self.initialize = initialize

class ClassDefBean(GenericBean):
    
    def __init__(self, classname, selfVars):
        """
        @className:str
        @selfVars:ScopeLevelBean
        """
        self.name = classname
        self.varinfo = selfVars
        self.FunDefArr = {} #of key = Fundef.name, FunDefBean for faster look up


class FunDefBean(GenericBean):
    
    def __init__(self, paramsTypes, returntype, fundefname):
        """
        @paramsTypes:*VarBean
        @returnType:VarBean
        @fundefname:str
        """
        self.typesparams = paramsTypes
        self.returnType = returntype
        self.name = fundefname
        self.numparams = len(paramsTypes) # this should be assigned after creation to be length of self.typesparams


class VarBean(GenericBean):
    
    def __inti__(self, name, aType):
        """
        @name:str
        @aType:str
        """
        self.varname = name
        self.vartype = aType


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
        @item:VarBean
        """
        return self.vars[item.name]
    
    def __contains__(self, item):
        """
        @item:VarBean
        @!bool
        """
        return item.name in self.vars
        
    def __iter__(self):
        return iter(self.vars)
        
    def append(self, item):
        """
        @item:VarBean
        """
        if(item.name in self.vars):
            print("reassign of " + item.name, file=sys.stderr)
        self.vars[item.name] = item
        
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
        