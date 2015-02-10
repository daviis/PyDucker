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
        self._first_visit()
        
    def _first_visit(self):
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
        value = self.visit(node.value)
        
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
            resultType = self.nameSpace.checkMagicMethod(target, value, op, node)
            return resultType
        except Exceptions.MissingMagicMethodException as ex:
            ex.lineno = node.lineno
            raise ex
        except KeyError:
            raise Exceptions.OutOfScopeException(target.name, node.lineno)    
            
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
        except Exceptions.MissingMagicMethodException as ex:
            ex.lineno = node.lineno
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
            if not self.nameSpace[aType].isBoolean(): #make sure that object can be evaluated as a boolean
                raise Exceptions.MissingMagicMethodException(node.lineno, self.nameSpace[aType]) #need to make a unop magic method excception
        return 'bool'
    
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
                raise Exceptions.IncorrectMethodExcepiton(clsBean, funcName, args, node.lineno)
        else:
            raise Exceptions.MissingMethodException(clsBean, funcName, node.lineno)

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
                    raise Exceptions.IncorrectMethodExcepiton(leftClass, op, arg.varType, node.lineno)
            else:
                raise Exceptions.MissingMethodException(leftClass, op, node.lineno)
        return Bean.VarBean('bool')
    
    def visit_Dict(self, node):
        print("need to figure out if we can tell what a dicts internals look like")
        return Bean.VarBean('dict')
    
    def visit_Eq(self, node):
        """
        @node:ast.ast        
        """
        return "__eq__"
    
    def visit_Expr(self, node):
        """
        @node:ast.ast
        """
        return self.visit(node.value)
    
    def visit_For(self, node):
        """
        @node:ast.ast
        """
        target = self.visit(node.target)
        anIter = self.visit(node.iter)
        
        if not self.nameSpace[anIter.varType].isIterable():
            raise Exceptions.MissingMethodException(self.nameSpace[anIter], '__iter__', node.lineno)
        
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
        if store:
                return Bean.VarBean(None, node.id)
        elif node.id in self.scope:
            return self.scope[node.id]
        else:
            raise Exceptions.OutOfScopeException(node.id, node.lineno)

    def visit_NameConstant(self, node):
        """
        @node:ast.ast
        """
        return Bean.VarBean(type(node.value).__name__)
        
    def visit_NotEq(self, node):
        """
        @node:ast.ast
        """
        return "__ne__"
             
    def visit_Num(self, node):
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

    def visit_Return(self, node):
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
            #Exceptions.MissingMagicMethodException(operandBean.name, op, node.lineno)
            print('Error found when trying to '+ op + ' on ' + operand +'.')#,file = sys.stderr)

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
        
