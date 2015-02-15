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
                 
    """
    Each individual vist_* will need to check if the result if a list, if so then 
    iterate over it. If not, then a single visit is needed
    """
    
    def visit_Delete(self, node):
        """
        @node:ast.ast
        Testing this one
        """
        print(ast.dump(node))
        print(node.targets)
        for i in node.targets:
            self.visit(i)
        print('visited')
        
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
            tars.append(self.visit(target))
        
        try:
            value = self.visit(node.value)
        except Exceptions.TypeMisMatchException as ex:
            ex.varName = tars[0].name
            raise ex
            
        for varBean in tars:
            if varBean.typesMatch(value):
                value.name = varBean.name
                self.scope[value.name] = value
            else:
                raise  Exceptions.TypeMisMatchException(varBean.name, varBean.varType, value.varType, node.lineno)
                

            
    def visit_Attribute(self, node):
        """
        Value is the varType of the object the function is being called on. node.attr is the str rep of 
        the method name
        """
        value = self.visit(node.value)
        ctx = self.visit(node.ctx)
        return value, node.attr
    
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
    
    def visit_Call(self, node):
        """
        When a method is called on a class it generates one of these. This will attempt to return the str rep of the return varType of the function.
        It can throw a MissingMethodException if the function isn't found in the class or if the number/types of paramiters is wrong
        @node:ast.ast
        """
        cls, funcName = self.visit(node.func)
        
        args = []
        for arg in node.args:
            args.append(self.visit(arg))
            
        keywords = []
        for key in node.keywords:
            keywords.append(self.visit(key))
            
        starargs = self.visit(node.starargs)
        kwargs = self.visit(node.kwargs)
        
        clsBean = self.nameSpace[cls.varType]
        if clsBean.hasFun(funcName):
            #fundefbean will need to be extended to handle things other than just a fixed lenght number of params
            if clsBean.funs[funcName].takes(args):
                return clsBean.funs[funcName].returnType
            else:
                raise Exceptions.IncorrectMethodExcepiton(funcName, args, node.lineno, aCls=cls)
        else:
            raise Exceptions.MissingMethodException(cls, funcName, node.lineno)

    def visit_Compare(self, node):
        """
        @node:ast.ast
        Need to be able to handle 1 < 2 < 3 as well as (1 < 2) < 3
        For the use of the phrase "x in y" the types of operator and operand need to be flipped. In generates the function "__contains__"
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
            
            leftClass = self.nameSpace[left.varType]
            if leftClass.hasFun(op):
                if leftClass.funs[op].takes([arg]):
                    left = arg
                else:
                    raise Exceptions.IncorrectMethodExcepiton(op, arg.varType, node.lineno, left)
            else:
                raise Exceptions.MissingMethodException(left, op, node.lineno)
        return Bean.VarBean('bool')
    
    def visit_Continue(self, node):
        """
        @node:ast.ast
        This node also does nothing.
        """
        return
    
    def visit_Dict(self, node):
        print("need to figure out if we can tell what a dicts internals look like")
        return Bean.VarBean('dict')
    
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
        self.scope.append(typeBean) #name will be a str var name that the exception will take on, we will need to add it to the scope then remove it from scope when the call completes.
        for bod in node.body:
            self.visit(bod)
        
    
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
    
    def visit_List(self, node):
        """
        @node:ast.ast
        """
        bean = Bean.VarBean('list')
        
        elements = []
        for ele in node.elts:
            elements.append(self.visit(ele))
        
        if all(x == elements[0] for x in elements):
            bean.homo = True
            bean.compType = [elements[0]]
        else:
            bean.compType = elements
            
        return bean
    
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
            scopedVarBean = self.scope[node.id]
            return scopedVarBean
        except KeyError:
            if store:
                return Bean.VarBean(None, node.id)
            else:
                raise Exceptions.OutOfScopeException(node.id, node.lineno)
            
    def visit_NameConstant(self, node):
        """
        @node:ast.ast
        """
        return Bean.VarBean(type(node.value).__name__)
        
    def visit_Not(self, node):
        """
        @node:ast.ast
        """
        return "__bool__"
        
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
        visit_pass has pass because pass does not do anything
        '''
        self.visit(node)
        
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
    
    def visit_UAdd(self,node):
        return('__pos__')
    
    def visit_UnaryOp(self,node):
        operand = self.visit(node.operand)
        operandBean = self.nameSpace[operand.varType]
        op = self.visit(node.op)
        if operandBean.hasFun(op):
            return operandBean.funs[op].returnType
        else:
            #Need an exception for unary ops
            Exceptions.MissingMagicMethodException(operandBean.name, op, node.lineno)
#             print('Error found when trying to '+ op + ' on ' + operand +'.')#,file = sys.stderr)

    def visit_USub(self,node):
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
        clsWalker = ClassDefWalker(node, self.nameSpace, self.scope.copy())
        clsWalker.walk()
        
        self.nameSpace.put(clsWalker.name, clsWalker.createClassBean())
        
         
    def visit_FunctionDef(self, node):
        """
        @node:ast.AST
        """
        funWalker = FunDefWalker(node, self.nameSpace, self.scope.copy())   
        funWalker.walk()
             
        self.nameSpace.put(funWalker.name, funWalker.createFunBean())
        
        print("out fun")
         
            
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
        self.name = funRoot.name
        self.retType = None
        self.nameSpace = nameSp
        
    def walk(self):
        self.visit(self.root)
        
    def _findParamTypes(self):
        scopeObject = parseDocString(ast.get_docstring(self.root))
    
    def createFunBean(self):
        bean = Bean.FunDefBean(list(self.scope), self.retType, self.name)
#         stuff about making the bean
        return bean
    
    def visit_FunctionDef(self, node):
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for arg in value:
                    self.visit(arg)
            elif value:
                self.visit(value)
            
    def visit_Return(self, node):
        #may need to look at the other fields in ast.Return but the basic way is this. 
        self.retType = self.visit(node.value)
        
        
    def visit_arguments(self,node):
        """
        @node:ast.ast
        """
        print('found visit_arguments')
        #print(ast.dump(node))
        arguments = parseDocString(ast.get_docstring(self.root))
        for i in arguments:
            self.scope.append(i)
            #Not the correct way to add it to the scope since we can't
            #remove it when we're done!
        print(self.scope.vars)
        print('done visitng_aruments')    
        
