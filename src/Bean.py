class ClassDefBean():
    
    def __init__(self, classname):
        self.classname = classname
        self.varinfo = {}
        self.FunDefobject = []

    def classname(self):
        return self.classname

    def varinfo(self):
        return self.varinfo

    def addvarinfo(self, varname, vartype):
        self.varinfo[varname] = vartype
    
    def FunDefobject(self):
        return self.FunDefobject
    
    def addFunDefobject(self, FunDefobject):
        self.FunDefobject.append(FunDefobject)

class FunDefBean():
    
    def __init__(self, returntype, fundefname):
        self.numparams = 0
        self.typesparams = []
        self.returntype = returntype
        self.fundefname = fundefname

        
    def numparams(self):
        return(self.numparams)

    def addnumparams(self):
        self.numparams = self.numparams + 1 

    def typesparmas(self):
        return self.typesparmas
    
    def addtypesparams(self, typeparam):
        self.typesparams.append(typeparam)

    def returntype(self):
        return self.returntype
    
    def fundefname(self):
        return self.fundefname

class VarBean():
    
    def __inti__(self, varname, vartype):
        self.varname = varname
        self.vartype = vartype
        
    def varname(self):
        return self.varname

    def vartype(self):
        return self.vartype

    
class GenericBean():
    
    def __inti__(self, name, initialize):
        self.name = name
        self.initialize

    def name(self):
        return self.name

    def initialize(self):
        return self.initialize
