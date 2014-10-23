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
        @selfVars:VarBean*
        """
        self.name = classname
        self.varinfo = LevelBean(selfVars)
        self.FunDefArr = {} #of key = Fundef.name, FunDefBean for faster look up


class FunDefBean(GenericBean):
    
    def __init__(self, paramsTypes, returntype, fundefname):
        """
        @paramsTypes:VarBean*
        @returnType:VarBean
        @fundefname:str
        """
        self.typesparams = LevelBean(paramsTypes)
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


class LevelBean(GenericBean):
    
    def __inti__(self, incomingVars = None):
        """
        
        """
        self.vars = {} #key will be the varName, value will be the VarBeanReference 
        if incomingVars:
            for var in incomingVars:
                self.append(var)
        
    def __getitem__(self, item):
        """
        @item:VarBean
        """
        return self.vars[item.name]
    
    def __conains__(self, item):
        """
        @item:VarBean
        """
        return item.name in self.vars
        
    def append(self, item):
        """
        @item:VarBean
        """
        if(item.name in self.vars):
            print("reassign of " + item.name, file=sys.stderr)
        self.vars[item.name] = item
        
        