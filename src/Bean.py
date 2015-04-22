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


class FunDefBean(GenericBean):
    
    def __init__(self, paramsTypes, returntype, fundefname, someKwargs = {}, someStarargs = None, minParams = 0):
        """
        @paramsTypes:*VarBean
        @returnType:VarBean
        @fundefname:str
        @someKwargs:str**VarBean
        @someStarargs:VarBean
        @minParams:int
        """
        self.typesparams = paramsTypes
        self.returnType = returntype
        self.name = fundefname
        self.starargs = someStarargs
        self.kwargs = someKwargs
        self.minNumParams = minParams
        self.scopeModifier = ""
        
    def clone(self):
        retBean = FunDefBean(self.typesparams, self.returnType, self.name, self.kwargs, self.starargs, self.minNumParams)
        return retBean
        
    def getParamType(self, idx):
        """
        @idx:int
        """
        if idx < len(self.typesparams)-1:
            return self.typesparams[idx]
        else:
            if self.typesparams[-1].varType == '$rept':
                return self.typesparams[-2]
            else:
                return self.typesparams[-1]
            
    def equals(self, namespace, fun):
        """
        @namespace:NameSpaceBean
        @fun:FunDefBean
        """
        return self._takes(namespace, fun.typesparams, fun.kwargs, fun.starargs)

    def _takes(self, namespace, paramList, kwargs, starargs):
        """
        @namespace:NameSpaceBean
        @paramList:VarBean*
        @kwargs:str**VarBean
        @starargs:VarBean*
        todo clean up this wayyyyyyyy to complicated logic
        """
        self._checkKwargs(kwargs)
        #there were starred arguments passed into the called function but, we can't check the length of them yet so just kind of go with the flow. 
        if starargs:
            for bothIdx in range(len(paramList)):
                if not namespace.checkImplicitTypeConversion(paramList[bothIdx], self.getParamType(bothIdx)):
                    return False
            bothIdx += 1
            if bothIdx == len(self.typesparams) and self.typesparams[-1] != VarBean("$rept"): #there are too many args when the starred args are unpacked. Figure that out here and return false because of it
                return False
            for selfIdx in range(bothIdx, len(self.typesparams)):
                if not namespace.checkImplicitTypeConversion(starargs.nextSubType(), self.getParamType(selfIdx)):
                    return False
            return True
        #there are not any starred arguments so just check the args one for one. 
        else:
            #Check to see if there are the right number of paramaters, keeping in mind the kwargs that were passed in.
            if len(paramList) < self.minNumParams:
                return False #could possibly make a more helpful statemetn here, but its functional for now.
            for bothIdx in range(len(paramList)):
                if not namespace.checkImplicitTypeConversion(paramList[bothIdx], self.getParamType(bothIdx)):
                    return False
            return True
    
    def _checkKwargs(self, kwargs):
        """
        @kwargs:str**VarBean
        """
        for key in kwargs:
            aVarBean = kwargs[key]
            aVarBean.name = key
            if key not in self.kwargs:
                raise Exceptions.IncorrectMethodKeywordException(aVarBean)
            if kwargs[key] != self.kwargs[key]:
                raise Exception.IncorrectMethodKeywordException(aVarBean)
             

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
        self.scopeModifier = "" #possible options for this will be global and nonlocal.
        self.valType = None
        
    def __eq__(self, other):
        if self.varType and other.varType:
            return self.varType == other.varType
        else:
            return True
    
    def nextSubType(self):
        if self.homo:
            return self.compType[0]
        else:
            raise Exceptions.HeteroCollecionException(self.name)
#             return self.compType
            
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
            
    def recursiveClone(self, otherBean):
        """
        @otherBean:VarBean
        Used for the assignment of objects so name shouldn't be cloned. 
        """
        self.homo = otherBean.homo
        self.varType = otherBean.varType
        self.starred = otherBean.starred
        if otherBean.valType:
            self.valType = otherBean.valType
        
        #copy the contents of the sub lists
        for compTypeObj in otherBean.compType:
            internalBean = VarBean(None)
            internalBean.recursiveClone(compTypeObj)
            self.compType.append(internalBean)
            

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
        for level in reversed(self.levels):
            if item in level:
                try:
                    if level[item].varType:
                        return level[item]
                    else:
                        raise Exceptions.RefBeforeAssignException(item)
                except AttributeError: #it will get a attributeerror from FunDefBeans, but that isn't a big error so just return it.  
                    return level[item]
            
        raise Exceptions.OutOfScopeException(item)
            
            
    
    def __setitem__(self, name, item):
        """
        Set a variable in the highest level of scope
        """
        currentLevel = self.levels[-1]
        currentLevel[name] = item
        
    def __delitem__(self,item):
        """
        @item:str
        Delete an entry from scope where item is the key
        """
        currentLevel = self.levels[-1]
        del currentLevel[item]
        
    def __contains__(self, item):
        """
        @item:str
        @!bool
        """
        currentLevel = self.levels[-1]
        return item in currentLevel
        
    def __iter__(self):
        currentLevel = self.levels[-1]
        return iter(currentLevel)
        
    def append(self, item):
        """
        @item:VarBean
        """

        currentLevel = self.levels[-1]
        
        if item.name in currentLevel and item != currentLevel[item.name]:
            print("reassign of " + item.name, file=sys.stderr)
            raise Exception()
            
        if item.name in currentLevel and currentLevel[item.name].scopeModifier:
            item.scopeModifier = currentLevel[item.name].scopeModifier    

        
        currentLevel[item.name] = item
        
    def goDownLevel(self):
        """
        Used when entering a function, it adds a dictionary to the stack of scope levels
        """
        self.levels.append({})
    
    def goUpLevel(self):
        """
        Used when leaving a function, it pops a dictionary to the stack of scope levels
        """
        if len(self.levels) > 1:
            return self.levels.pop()
        else:
            raise Exception("Can't leave the global scope")
        
    def makeNonlocalReference(self, names):
        """
        @names:VarBean*
        """
        if len(self.levels) < 2:
            raise Exceptions.NonlocalReferenceException(names, "Not enough levels of scope to make a nonlocal reference. Maybe a 'global' call would work")
        #there is the possibility of finding the variable name check everywhere but the global scope
        for nameBean in names:
            if self._nonlocalGlobalAlreadyUsedCheck(nameBean): #if the variable is already in scope at this level then it will not work.
                raise Exceptions.NonlocalReferenceException([nameBean], "Name assigned before nonlocal declaration.")
            else:
                for level in reversed(self.levels[1:]): #look in every level except for the global scope
                    if nameBean.name in level:
                        if nameBean.scopeModifier == "global":
                            raise Exceptions.NonlocalReferenceException([nameBean], "There variable was previously pulled out of the global scope. The global keyword may serve you better.")
                        else:
                            nameBean.recursiveClone(level[nameBean.name])
                            nameBean.scopeModifier = "nonlocal"
                            self.append(nameBean)
                            return #don't need to return anything, just return so the last of the loop isn't used 
                    else:
                        continue #keep going until the end of the lists
         
    
    def makeGlobalReference(self, names):
        """
        @names:VarBean*
        """
        for nameBean in names:
            if self._nonlocalGlobalAlreadyUsedCheck(nameBean):
                raise Exceptions.GlobalReferenceException(nameBean, "Name assigned before global declaration.")
            else:
                globSpace = self.levels[0]
                if nameBean.name not in globSpace:
                    raise Exceptions.ScopeNotFoundException("Global", nameBean)
                else:
                    nameBean.scopeModifier = "global"
                    self.append(nameBean)
                 
        
    def _nonlocalGlobalAlreadyUsedCheck(self, nameBean):
        """
        @nameBean:VarBean
        
        Helper function for both global and nonlocal keywords.
        """
        if nameBean.name in self.levels[-1]:
            return True
        else:
            return False
        
    def addClassInit(self, clsWalker):
        """
        @clsWalker:Walker.ClassDefWalker
        """
        initFun = clsWalker.initFun.clone()
        initFun.name = clsWalker.name
        self.append(initFun)
     
class ClassDefBean(GenericBean):
    
    def __init__(self, classname, selfVars, someDataMembers, rent = 'object'):
        """
        @className:str
        @selfVars:ScopeLevelBean
        @rent:str
        @someDataMembers:ScopeLevelBean
        """
        self.initFun = None
        self.name = classname
        self.varinfo = selfVars
        self.dataMembers = someDataMembers
        self.parent = rent #the name of the parent varType
        
    def hasFun(self, op):
        """
        @op:str
        """
        return op in self.dataMembers
    
    def acceptsFun(self, fun, namespace):
        """
        @fun:FunDefBean
        """
        try:
            if self.dataMembers[fun.name].equals(namespace, fun):
                return self.dataMembers[fun.name].returnType
            else:
                raise Exceptions.IncorrectMethodException(fun.name, fun.typesparams, aCls = VarBean(self.name), kws = fun.kwargs, star = fun.starargs)
        except KeyError:
            raise Exceptions.MissingMethodException(self, fun.name)
        except Exceptions.IncorrectMethodKeywordException as ex:
            ex.fun = fun.name
            ex.cls = VarBean(self.name)
            raise ex
            
    def isIterable(self):
        if not "__iter__" in self.dataMembers:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__iter__")

    def isCallable(self):
        if not "__call__" in self.dataMembers:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__call__")
    
    def isString(self):
        if not "__str__" in self.dataMembers:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__str__")
    
    def isBoolean(self):
        if not "__bool__" in self.dataMembers:
            raise Exceptions.MissingMethodException(VarBean(self.name), "__bool__")
               
        
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
        
    def duckCallable(self, varBean):
        """
        @varBean:VarBean
        """
        self.vars[varBean.varType].isCallable()
        
    def addFirstClassFun(self, funDefBean):
        """
        @funDefBean:FunDefBean
        """
        funsClass = self.vars["$funs"]
        funsClass.funs[funDefBean.name] = funDefBean
    
    def checkImplicitTypeConversion(self, typeFound, typeNeeded):
        """
        @typeFound:VarBean
        @typeNeeded:VarBean
        """
        if typeFound.varType == typeNeeded.varType:
            return True
        #elif check to see if the super class works
        elif self.vars[typeFound.varType].parent:
            newVarType = self.vars[typeFound.varType].parent
            done = False
            while not done:
                if newVarType == typeNeeded.varType:
                    return True
                else:
                    if self.vars[typeFound.varType].parent:
                        newVarType = self.vars[typeFound.varType].parent
                    else:
                        done = True
                        foundCls = self.vars[typeFound.varType]
                        neededConverter = "__" + typeNeeded.varType + "__"
                        if foundCls.hasFun(neededConverter):
                            return True
                        else:
                            return False
    
        
    def addClassesClass(self, funDefClass):
        """
        @funDefClass:FunDefBean
        fundefbean will be a copy of __init__ fundefbean who's name has been changed to the classes name.
        """
        classesClass = self.vars["$classes"]
        classesClass.dataMembers.append(funDefClass)
     
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
                resultType = self.vars[bean.varType].acceptsFun(fun, self)
                return resultType
            except Exceptions.MissingMethodException:
                pass
        raise Exceptions.MissingMagicMethodException(lbean, rbean, op, rOp)
            
