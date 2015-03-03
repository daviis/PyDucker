'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast
import sys
import Bean
import Exceptions
from DocStringParser import parseDocString

class InitialWalker(ast.NodeVisitor):
    def __init__(self, astNode, nameSp, scopeBean):
        """
        @astNode:ast.AST
        @nameSp:Bean.NameSpaceBean
        @scopeBean:Bean.ScopeLevelBean
        """
        self.root = astNode
        self.nameSpace = nameSp
        self.scope = scopeBean
        
    def walk(self):
        self.visit(self.root)
        
    def generic_visit(self, node):
        """
        Called if no explicit visitor function exists for a node.
        """
        if isinstance(node, ast.AST):
            print("Unknown varType of ast node. Need to implement visit_" + node.__class__.__name__, file=sys.stderr)
            super().generic_visit(node)
        #set a break point on this to find where there is a need to list-ify a vist_
        elif isinstance(node, list):
            print('got a list', file=sys.stderr)
            
    def _makeCompType(self, nodeList):
        """
        @nodeList:ast.ast*
        Used for creating lists, sets and tuples.
        """
        elements = []
        for ele in nodeList:
            elements.append(self.visit(ele))
        
        if all(x == elements[0] for x in elements):
            if elements:
                return [elements[0]]
            else:
                return elements #this will be an empty list because the  iterable it is going into is empty 
        else:
            return elements
                 
    def _generatorHelper(self, varBean, ele):
        """
        @varBean:Bean.VarBean
        @ele:ast.ast
        """
        varBean.compType = [self.visit(ele)]
        
        for internalType in varBean.compType:
            internalType.name = '_' #clear out the name that was in comp type
        
        if len(varBean.compType) == 1:
            varBean.homo = True
            
        return varBean
    
    def _tupleUnpacking(self, tupleOfVarNames, target):
        """
        @tupleOfVarnames:Bean.VarBean
        @target:Bean.VarBean
        A helper function for visit_Assign. This function handles tuple unpacking and adding the new vars to the scope. 
        Part of tuple unpacking is making sure that Starred values keep their comp type
        @todo handle lists of variable types, then we can also add in length checking (maybe)
        """
        self.nameSpace.duckIter(target)
        
        for varBean in tupleOfVarNames.compType: 
            if varBean.starred:
                if target.homo:
                    varBean.compType = target.compType
                    varBean.homo = True
                    varBean.starred = False
                    self.scope.append(varBean)
                else:
                    raise Exceptions.PyDuckerException(-1) #we cant do non homo lists like this. If we want to do them at some point then we will need to extend this fun.
            else:
                compBean = target.compType[0] 
                compBean.name = varBean.name
                self.scope.append(compBean)
            
                 
    """
    Each individual vist_* will need to check if the result if a list, if so then 
    iterate over it. If not, then a single visit is needed
    """
 
        
    def visit_Add(self, node):
        """
        @node:ast.ast
        
        Usually a binop will call this and return a str rep of the magic method __add__
        """
        return "__add__"
    
    def visit_And(self, node):
        """
        @node:ast.ast
        """
        return "__and__"
    
    def visit_Assert(self, node):
        """
        @node:ast.ast
        """
        testType = self.visit(node.test)
        try:
            self.nameSpace.duckBool(testType) #check to see if the condition will evaluate to a boolean type, if not an exception is thrown
            msgType = self.visit(node.msg)
            self.nameSpace.duckStr(msgType) #check to see if msgType will evaluate to a string, if not an exception is thrown.
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
     
    def visit_Assign(self, node):
        """
        @node:ast.ast
        @todo look into tuple unpacking here
        
        Targets are the things on the left hand side of the assignment statement. Value will be what is on the right side.
        If there is a reassignment of a variables varType within one varbean it will throw a TypeMisMatchException
        """
        tars = []
        for target in node.targets:
            newVarName = self.visit(target)
            tars.append(newVarName)
            self.scope.append(newVarName)
        
        try:
            value = self.visit(node.value)
        except Exceptions.TypeMisMatchException as ex:
            ex.varName = tars[0].name
            raise ex
            
        for varBean in tars:
            
            if varBean.varType == "tuple" and varBean.starred:
                try:
                    self._tupleUnpacking(varBean, value)
                except Exceptions.PyDuckerException as ex:
                    ex.lineNum = node.lineno
                    raise ex
                
            elif varBean.typesMatch(value):
                varBean.recursiveClone(value)
#                 value.name = varBean.name
                self.scope.append(varBean)
            
            else:
                raise  Exceptions.TypeMisMatchException(varBean.name, varBean.varType, value.varType, node.lineno)
                

            
    def visit_Attribute(self, node):
        """
        Value is the varType of the object the function is being called on. node.attr is the str rep of 
        the method name
        """
        return node.attr
#         value = self.visit(node.value)
#         ctx = self.visit(node.ctx)
#         return value, node.attr
    
    def visit_AugAssign(self, node):
        """
        @node:ast.ast
        """
        target = self.visit(node.target)
        op = self.visit(node.op)
        value = self.visit(node.value)
        
        try:
            resultType = self.nameSpace.checkMagicMethod(target, value, op)
            return resultType
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
        except KeyError:
            raise Exceptions.OutOfScopeException(target.name, lineNo = node.lineno)    
            
    def visit_BinOp(self, node):
        """
        This will return the varType of the function that is being called. Could throw MissingMethodException if the magic method cant be found.
        @node:ast.ast
        """
        leftBean = self.visit(node.left)
        op = self.visit(node.op)
        rightBean = self.visit(node.right)
        
        try:
            resultType = self.nameSpace.checkMagicMethod(leftBean, rightBean, op)
            return resultType
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
         
    def visit_BitAnd(self, node):
        """
        @node:ast.ast
        """
        return "__and__"
    
    def visit_BitOr(self, node):
        """
        @node:ast.ast
        """
        return "__or__"
    
    def visit_BitXor(self, node):
        """
        @node:ast.ast
        """
        return "__xor__"
         
    def visit_BoolOp(self, node):
        """
        @node:ast.ast
        We have the chance to find unreachable code here. It isn't necessary to keep track of op if we dont.
        """
        op = self.visit(node.op)
        valueList = []
        for val in node.values:
            valueList.append(self.visit(val))
            
        for aType in valueList:
            try:
                self.nameSpace.duckBool(aType) #make sure that object can be evaluated as a boolean, if it isn't an internal exception is raised
            except Exception.PyDuckerException as ex:
                ex.lineNum = node.lineno
                raise ex
        return 'bool'
    
    def visit_Break(self, node):
        """
        @node:ast.ast
        this node doesn't do anything
        """
        return
    
    def visit_Bytes(self, node):
        """
        @node:ast.ast
        """
        return Bean.VarBean('bytes')
    
    def visit_Call(self, node):
        """
        When a method is called on a class it generates one of these. This will attempt to return the str rep of the return varType of the function.
        It can throw a MissingMethodException if the function isn't found in the class or if the number/types of paramiters is wrong
        @node:ast.ast
        """
        funcName = self.visit(node.func) #this will be an ast.Attribute for `'a'.upper()` or a ast.Name for `'a'() or print()`
        
        args = []
        for arg in node.args:
            args.append(self.visit(arg))
            
        keywords = []
        for key in node.keywords:
            keywords.append(self.visit(key))
            
        starargs = self.visit(node.starargs)
        kwargs = self.visit(node.kwargs)

        try:
            #assume that the function will be part of a class, so try to look up the class type, then see if it has the function.
            cls = self.visit(node.func.value)
            clsBean = self.nameSpace[cls.varType]
            funBean = Bean.FunDefBean(args, None, funcName)
            return clsBean.acceptsFun(funBean)
        
        except AttributeError:
            #there wasn't a class to find (attribute error from ast.Attribute), check to see if it is a global
            #todo look up in scope to make sure that the params match
            #todo make it do a scope look up to see if the funcName is a str b/c then it will need to do a scope look up.
            return funcName.returnType
        
            
#         todo clean up
#         if clsBean.hasFun(funcName):
#             #fundefbean will need to be extended to handle things other than just a fixed lenght number of params
#             if clsBean.funs[funcName].takes(args):
#                 return clsBean.funs[funcName].returnType
#             else:
#                 raise Exceptions.IncorrectMethodExcepiton(funcName, args, node.lineno, aCls=cls)
#         else:
#             raise Exceptions.MissingMethodException(cls, funcName, node.lineno)

    def visit_Compare(self, node):
        """
        @node:ast.ast
        Need to be able to handle 1 < 2 < 3 as well as (1 < 2) < 3
        For the use of the phrase "x in y" the types of operator and operand need to be flipped. In generates the function "__contains__"
        @todo refactor the fundef checking down into the namespace
        """
        left = self.visit(node.left)
        
        zipped = zip(node.ops, node.comparators)

        for pair in zipped:
            op = self.visit(pair[0])
            arg = self.visit(pair[1])
            
            if op == "__contains__":
                temp = arg
                arg = left
                left = temp
                
            elif op == "is" or op == "isnot":
                continue
            
            leftClass = self.nameSpace[left.varType]
            if leftClass.hasFun(op):
                if leftClass.funs[op].takes([arg]):
                    left = arg
                else:
                    raise Exceptions.IncorrectMethodExcepiton(op, arg.varType, node.lineno, left)
            else:
                raise Exceptions.MissingMethodException(left, op, node.lineno)
        return Bean.VarBean('bool')
    
    def visit_comprehension(self, node):
        """
        @node:ast.ast
        @todo figure out what node.ifs is supposed to do.
        """
        targetVar = self.visit(node.target)
        
        for anIf in node.ifs:
            self.visit(anIf)
        
        iterVar = self.visit(node.iter)
        try:
            self.nameSpace.duckIter(iterVar)
            if iterVar.homo:
                retVar =  iterVar.compType[0]
                retVar.name = targetVar.name
                self.scope.append(retVar)
            else:
                print("Not sure how we are doing non homo lists.", file=sys.stderr)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
    
    def visit_Continue(self, node):
        """
        @node:ast.ast
        This node also does nothing.
        """
        return
    
    def visit_Del(self, node):
        """
        @node:ast.ast
        Doesn't do anything
        May come into play when deleting via splice and index
        instead of a full list
        """
        return       
    
    def visit_Delete(self, node):
        """
        @node:ast.ast
        Much like visit_Assign instead of adding we remove it from the scope
        """  
        tars = []
        for target in node.targets:
            tars.append(self.visit(target)) 
            
        for varBean in tars:
            if varBean.name in self.scope:
                del self.scope[varBean.name]
            else: #Very small chance to actually get here
                #the visit_Name function will catch out of scope first
                raise Exceptions.OutOfScopeException(target.name, lineNo = node.lineno)
    
    def visit_Dict(self, node):
        """
        @node:ast.ast
        @todo finalize the internal structure of the varbean being returned.
        """
        keyTypes = self._makeCompType(node.keys)
        valTypes = self._makeCompType(node.values)
        retBean =  Bean.VarBean('dict')
        
        if len(keyTypes) == 1:
            retBean.homo = True
        retBean.compType = keyTypes
        
        if len(valTypes) == 1:
            pass #maybe have a second internal homo variable?
        retBean.valType = valTypes
        
        return retBean
    
    def visit_DictComp(self, node):
        """
        @node:ast.ast
        """
        retBean = Bean.VarBean('dict')
        
        for gen in node.generators:
            self.visit(gen)
        retBean.compType = [self.visit(node.key)]
        retBean.valType = [self.visit(node.value)]
        
        return retBean
    
    def visit_Div(self, node):
        """
        @node:ast.ast
        """
        return "__div__"
    
    def visit_Eq(self, node):
        """
        @node:ast.ast        
        """
        return "__eq__"
    
    def visit_ExceptHandler(self, node):
        """
        @node:ast.ast
        todo maybe need to pop the the exception name from scope after this call
        """
        typeBean = self.visit(node.type)
        typeBean.name = node.name
        
        self.scope.goDownLevel()
        
        self.scope.append(typeBean) #name will be a str var name that the exception will take on, we will need to add it to the scope then remove it from scope when the call completes.
        for bod in node.body:
            self.visit(bod)
        
        self.scope.goUpLevel()
    
    def visit_Expr(self, node):
        """
        @node:ast.ast
        """
        return self.visit(node.value)
    
    def visit_FloorDiv(self, node):
        """
        @node:ast.ast
        """
        return "__floordiv__"
    
    def visit_For(self, node):
        """
        @node:ast.ast
        """
        target = self.visit(node.target)
        anIter = self.visit(node.iter)
        
        try:
            self.nameSpace.duckIter(anIter)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
        
        target.varType = anIter.nextSubType()
        self.scope.append(target)
        
        for bod in node.body:
            self.visit(bod)
        return 
 
    def visit_GeneratorExp(self, node):
        """
        @node:ast.ast
        """
        for gen in node.generators:
            self.visit(gen)
            
        return self._generatorHelper(Bean.VarBean("generator"), node.elt)
    
    def visit_Global(self, node):
        """
        @node:ast.ast
        """
        varNames = []
        for nameNode in node.names:
            varNames.append(Bean.VarBean(None, nameNode))
                    
        try:
            self.scope.makeGlobalReference(varNames)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
        
    def visit_Gt(self, node):
        """
        @node:ast.ast
        """
        return "__ge__"
    
    def visit_GtE(self, node):
        """
        @node:ast.ast        
        """
        return "__ge__"

    def visit_If(self,node):
        """
        @node:ast.ast
        """
        self.visit(node.test)
        
        for body in node.body:
            self.visit(body)
        
        for orElse in node.orelse:
            self.visti(orElse)
            
    def visit_IfExp(self, node):
        """
        @node:ast.ast
        """
        testVal = self.visit(node.test)
        try:
            self.nameSpace.duckBool(testVal)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex
        
        first = self.visit(node.body)
        second = self.visit(node.orelse)
        if first == second:
            return first
        else:
            raise Exceptions.TypeMisMatchException("_", first, second, node.lineno)
        
    def visit_In(self, node):
        '''
        visit_In returns __contains__ unless something else is found because
        In is almost the same as asking if someting __contains__ something.
        '''
        return '__contains__'
    
    def visit_Invert(self,node):
        """
        @node:ast.ast
        """
        return('__invert__')
    
    def visit_Is(self, node):
        """
        @node:ast.ast
        Is isn't actually a magic method, it calls id() on the objects, which in cpython returns the mem-address of each obj. Then compares them. 
        It would be possible to check to see if each side was of the same type and if they wernt then they couldn't possibly be the same mem address and throw an exception. But this is the safe way for now.
        """
        return "is"
    
    def visit_IsNot(self, node):
        """
        @node:ast.ast
        Is not is just the same as is then inverted.
        """
        return "isnot"
        
    
    def visit_List(self, node):
        """
        @node:ast.ast
        """
        bean = Bean.VarBean('list')
        
        elements = self._makeCompType(node.elts)
        
        if len(elements) == 1:
            bean.homo = True
        bean.compType = elements
            
        return bean
    
    def visit_ListComp(self, node):
        """
        @node:ast.ast
        """
        for gen in node.generators:
            self.visit(gen)
            
        return self._generatorHelper(Bean.VarBean('list'), node.elt)
        
    def visit_Load(self, node):
        """
        @node:ast.ast
        This is an empty ast node, it just denodes that the name will be loading from namespace
        """
        return False
    
    def visit_LShift(self, node):
        """
        @node:ast.ast
        """
        return "__lshift__"
    
    def visit_Lt(self, node):
        """
        @node:ast.ast
        """
        return "__lt__"
    
    def visit_LtE(self, node):
        """
        @node:ast.ast
        """
        return "__le__"
    
    def visit_Mod(self, node):
        """
        @node:ast.ast
        """
        return "__mod__"
    
    def visit_Module(self, node):
        for bod in node.body:
            self.visit(bod)
    
    def visit_Mult(self, node):
        return "__mul__"
    
    def visit_Name(self, node):
        """
        @node:ast.ast
        Store will be a boolean for if the Name is going to be loaded from or stored to the namespace.
        It will return a VarBean related to the assign 
        """
        store = self.visit(node.ctx)
        
        try:
            return self.scope[node.id]
        except Exceptions.PyDuckerException as ex:
            if store:
                return Bean.VarBean(None, node.id)
            else:
                ex.lineNum = node.lineno
                raise ex
            
    def visit_NameConstant(self, node):
        """
        @node:ast.ast
        """
        return Bean.VarBean(type(node.value).__name__)
        
    def visit_Nonlocal(self, node):
        """
        @node:ast.ast
        """
        varNames = []
        for nameNode in node.names:
            varNames.append(Bean.VarBean(None, nameNode))
            
        try:
            self.scope.makeNonlocalReference(varNames)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = node.lineno
            raise ex

    def visit_Not(self, node):
        """
        @node:ast.ast
        """
        return "__bool__"
    
    def visit_NotIn(self, node):
        """
        @node:ast.ast
        """
        return "__contains__"
        
    def visit_NotEq(self, node):
        """
        @node:ast.ast
        """
        return "__ne__"
             
    def visit_Num(self, node):
        """
        @node:ast.ast
        """
        return Bean.VarBean(type(node.n).__name__)
    
    def visit_Or(self, node):
        """
        @node:ast.ast
        """
        return "__or__"
     
    def visit_Pass(self, node):
        '''
        @node:ast.ast
        visit_pass has pass because pass does not do anything
        '''
        return
        
    def visit_Pow(self, node):
        """
        @node:ast.ast
        """
        return "__pow__"
    
    def visit_Raise(self, node):
        """
        @node:ast.ast
        """
        raisedType = self.visit(node.exc)
        self.visit(node.cause) #todo figure out what this is susposed to do. The syntax is "raise x from y"
    
    def visit_Return(self, node):
        """
        @node:ast.ast
        """
        #may need to look at the other fields in ast.Return but the basic way is this. 
        return self.visit(node.value)
    
    def visit_RShift(self, node):
        """
        @node:ast.ast
        """
        return "__rshift__"
    
    def visit_Set(self, node):
        """
        @node:ast.ast
        """
        bean = Bean.VarBean('set')
        
        elements = self._makeCompType(node.elts)
        if len(elements) == 1:
            bean.homo = True
            bean.compType = [elements[0]]
        else:
            bean.compType = elements
            
        return bean
    
    def visit_SetComp(self, node):
        """
        @node:ast.ast
        """
        for gen in node.generators:
            self.visit(gen)
        
        return self._generatorHelper(Bean.VarBean('set'), node.elt)
            
    def visit_Starred(self, node):
        """
        @node:ast.ast
        I think it will alwyas be false, otherwise just raise an exception
        """
        if self.visit(node.ctx): #if it was to store things into
            retBean = self.visit(node.value)
            retBean.varType = "list" 
            retBean.starred = True
            return retBean
        else:
            raise Exceptions.PyDuckerException(-1)
            
    def visit_Store(self, node):
        """
        @node:ast.ast
        This is an empty ast node, it just denodes that the name will be storing to namespace
        """
        return True
            
    def visit_Str(self, node):
        return Bean.VarBean('str')
    
    def visit_Sub(self, node):
        """
        @node:ast.ast
        """
        return "__sub__"
    
    def visit_Try(self, node):
        """
        @node:ast.ast
        """
        for bod in node.body:
            self.visit(bod)
        for hand in node.handlers:
            self.visit(hand)
        for orelse in node.orelse:
            self.visit(orelse)
        for final in node.finalbody:
            self.visit(final)
    
    def visit_Tuple(self, node):
        """
        @node:ast.ast
        A store will be on the left side of an assignment statement, like 'a, b = [1, 2]'
        In a store all the types will need to be a ast.Name type
        """
        store = self.visit(node.ctx)
        if store:
            retBean = Bean.VarBean('tuple')
            for ele in node.elts:
                retBean.compType.append(self.visit(ele))
            retBean.starred = True #set starred to true becuase unpacking needs a flag to show it isn't a reassign of a regular tuple
            return retBean
        else:
            retBean = Bean.VarBean("tuple")
            compType = self._makeCompType(node.elts)
            if len(compType) == 1:
                retBean.homo = True
            retBean.compType = compType
            return retBean
    
    def visit_UAdd(self,node):
        """
        @node:ast.ast
        """
        return('__pos__')
    
    def visit_UnaryOp(self,node):
        """
        @node:ast.ast
        """
        operand = self.visit(node.operand)
        operandBean = self.nameSpace[operand.varType]
        op = self.visit(node.op)
        if operandBean.hasFun(op):
            return operandBean.funs[op].returnType
        else:
            Exceptions.MissingMethodException(operandBean, op, node.lineno)

    def visit_USub(self,node):
        """
        @node:ast.ast
        """
        return('__neg__')
    
    def visit_While(self, node):
        """
        @node:ast.ast
        """
        self.visit(node.test)
        for bodyPart in node.body:
            self.visit(bodyPart) #i dont think this needs to store what gets returned
        for orelse in node.orelse:
            self.visit(orelse)
     
    #These are initial walker independent, ie they should be over written in inheriting classes    
    def visit_ClassDef(self, node):
        """
        @node:ast.AST
        """
        self.scope.goDownLevel()
        
        clsWalker = ClassDefWalker(node, self.nameSpace, self.scope)
        clsWalker.walk()
        
        self.nameSpace.put(clsWalker.name, clsWalker.createClassBean())
        
        self.scope.goUpLevel()
         
    def visit_FunctionDef(self, node):
        """
        @node:ast.AST
        """
        self.scope.goDownLevel()
        
        funWalker = FunDefWalker(node, self.nameSpace, self.scope)   
        funWalker.walk()
             
        self.scope.goUpLevel()
        self.scope.append(Bean.VarBean('function', funWalker.name))
            
class ClassDefWalker(InitialWalker):
    
    def __init__(self, classRoot, nameSp, scopeCopy):
        """
        @classRoot:ast.ast
        @nameSp:bean.NameSpaceBean
        @scopeCopy:bean.ScopeBean
        """
        super().__init__(classRoot, nameSp, scopeCopy)
        self.initFun = None
        self.parent = None
        self.funs = Bean.NameSpaceBean()
        self.name = classRoot.name
       
    def walk(self):
        #first call should be a quick walk to snag all of the fun names and self var names
        for bod in self.root.body:
            self.visit(bod)
        
    def visit_FunctionDef(self, node):
        """
        @node:ast.ast
        """
        self.funs.append(node)
        if(node.name == '__init__'):
            self.initFun = node
    
    def createClassBean(self):
        bean = Bean.ClassDefBean(self.name, self.funs, self.parent)
#         stuff about making the bean
        return bean
    
class FunDefWalker(InitialWalker):
    def __init__(self, funRoot, nameSp, scopeLevel):
        """
        @funRoot:ast.ast
        @nameSp:bean.NameSpaceBean
        @scopeLevel:bean.ScopeLevelBean
        """
        super().__init__(funRoot, nameSp, scopeLevel)
        self._findParamTypes()
        self.name = funRoot.name
        self.retType = None
        self.nameSpace = nameSp
        
    def walk(self):
        try:
            self.visit(self.root.args)
        except Exceptions.PyDuckerException as ex:
            ex.lineNum = self.root.lineno
            raise ex 
        
        for dec in self.root.decorator_list:
            self.visit(dec)
            
        for bod in self.root.body:
            self.visit(bod)           
            
        
    def _addPramsToScope(self):
        params = self._findParamsTypes()
        for scope in params:
                self.scope.append(scope)
        
    def _findParamTypes(self):
        if ast.get_docstring(self.root):
            return parseDocString(ast.get_docstring(self.root))
        else:
            return []
        
    def createFunBean(self):
        return Bean.FunDefBean(self._findParamTypes(), self.retType, self.name)
    
    def visit_Return(self, node):
        self.retType = self.visit(node.value)
        
    def visit_arguments(self,node):
        """
        @node:ast.ast
        """
        arglist = node.args
        if arglist != []:    
            if ast.get_docstring(self.root) != None:
                arguments = parseDocString(ast.get_docstring(self.root))
                for i in arguments:
                    self.scope.append(i)
            else:
                Exceptions.MissingDocStringException(self.name)
                
            #Not the correct way to add it to the scope since we can't
            #remove it when we're done!
        
