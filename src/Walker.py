'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast
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
        self.classes = []
        self.funs = []
        self.globals = []
        self.nameSpace = nameSp
        self.scope = scopeBean
        
    def walk(self):
        self._first_visit()
        
    def _first_visit(self):
        self.visit(self.root)
        
#     def generic_visit(self, node):
#         """
#         This function is to identify what type of visits should be made. 
#         The type(node).__name__ returns the word to append to visit_ 
#         to make a visitor
#         """
#         print (type(node).__name__)
#         ast.NodeVisitor.generic_visit(self, node)
        
    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node.
        ----
        Comment out this method if recursion depth is exceded
        It means that one of the vist_* methods in the test case
        is not implemented yet.
        ---
        """
        if isinstance(node, ast.AST):
            print("Unknown type of ast node. Need to implement visit_" + node.__class__.__name__)
            
        #set a break point on this to find where there is a need to list-ify a vist_
        elif isinstance(node, list):
            print('got a list')
         
         
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
     
    def visit_arg(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
            
    def visit_arguments(self, node):
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for arg in value:
                    self.visit(arg)
            elif value:
                self.visit(value)
                
    def visit_Assign(self, node):
        """
        @node:ast.ast
        @todo look into tuple unpacking here
        
        Targets are the things on the left hand side of the assignment statement. Value will be what is on the right side.
        If there is a reassignment of a variables type within one varbean it will throw a TypeMissMatchException
        """
        targets = []
        for target in node.targets:
            targets.append(self.visit(target))
        value = self.visit(node.value)
        
        for varBeanName in targets:
            curType = self.scope[varBeanName].type
            if value != curType and curType:
                raise  Exceptions.TypeMissMatchException(varBeanName, curType, value, node.lineno)
            else:
                self.scope[varBeanName].type = value

            
    def visit_Attribute(self, node):
        """
        Value is the type of the object the function is being called on. node.attr is the str rep of 
        the method name
        """
        value = self.visit(node.value)
        ctx = self.visit(node.ctx)
        return value, node.attr
            
    def visit_AugAssign(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
        
    def visit_UnaryOp(self,node):
        operand = self.visit(node.operand)
        operandBean = self.nameSpace[operand]
        op = self.visit(node.op)
        if operandBean.hasFun(op):
            return operandBean.funs[op].returnType
        else:
            print('Error found when trying to '+ op + ' on ' + operand +'.',file = sys.stderr)
    
    def visit_Invert(self,node):
        return('__invert__')
    
    def visit_UAdd(self,node):
        return('__pos__')
    
    def visit_USub(self,node):
        return('__neg__')
           
    def visit_BinOp(self, node):
        """
        This will return the type of the function that is being called. Could throw MissingMethodException if the magic method cant be found.
        @node:ast.ast
        """
        leftType = self.visit(node.left)
        op = self.visit(node.op)
        rOp = op[:2] + 'r' + op[2:]
        rightType = self.visit(node.right)
        print(op)
        #look up if the method is contained in the left, if not then maybe the right
        #if so, then return the return type of the function
        
        leftBean = self.nameSpace[leftType]
        rightBean = self.nameSpace[rightType]
        
        if leftBean.hasFun(op):
            if leftBean.funs[op].takes([rightType]):
                return leftBean.funs[op].returnType
        if rightBean.hasFun(rOp):
            if rightBean.funs[rOp].takes([leftType]):
                return rightBean.funs[rOp].returnType
        else:
            raise Exceptions.MissingMagicMethodException(leftBean.name, rightBean.name, op, rOp, node.lineno)
         
    def visit_Call(self, node):
        """
        When a method is called on a class it generates one of these. This will attempt to return the str rep of the return type of the function.
        It can throw a MissingMethodException if the function isn't found in the class or if the number/types of paramiters is wrong
        @node:ast.ast
        """
        cls, funcName = self.visit(node.func)
        
        args = []
        for arg in node.args:
            args.append(self.visit(arg))
            
        keywords = self.visit(node.keywords)
        starargs = self.visit(node.starargs)
        kwargs = self.visit(node.kwargs)
        
        clsBean = self.nameSpace[cls]
        if clsBean.hasFun(funcName):
            #fundefbean will need to be extended to handle things other than just a fixed lenght number of params
            if clsBean.funs[funcName].takes(args):
                return clsBean.funs[funcName].returnType
            else:
                raise Exceptions.IncorrectMethodExcepiton(clsBean.name, funcName, args, node.lineno)
        else:
            raise Exceptions.MissingMethodException(clsBean.name, funcName, node.lineno)
 
    def visit_Module(self, node):
        for _, value in ast.iter_fields(node):
            for item in value:
                self.visit(item)
             
    def visit_Expr(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
             
    def visit_For(self, node):
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for arg in value:
                    self.visit(arg)
            elif value:
                self.visit(value)
            
    def visit_Load(self, node):
        """
        @node:ast.ast
        This is an empty ast node, it just denodes that the name will be loading from namespace
        """
        return False

    def visit_Mult(self, node):
        return "__mul__"
    
    def visit_Name(self, node):
        """
        @node:ast.ast
        Store will be a boolean for if the Name is going to be loaded from or stored to the namespace.
        It will return a tuple that is the store boolean and the VarBean realted to the assign 
        """
        store = self.visit(node.ctx)
        if store:
            if not node.id in self.scope:
                bean = Bean.VarBean(node.id, None)
                self.scope.append(bean)
            return node.id
        else:    
            return self.scope[node.id].type
             
    def visit_Num(self, node):
        return type(node.n).__name__
     
    def visit_Return(self, node):
        #may need to look at the other fields in ast.Return but the basic way is this. 
        val = self.visit(node.value)
            
    def visit_Store(self, node):
        """
        @node:ast.ast
        This is an empty ast node, it just denodes that the name will be storing to namespace
        """
        return True
            
    def visit_Str(self, node):
        return "str"
     
    #These are initial walker independent, ie they should be over written in inheriting classes    
    def visit_ClassDef(self, node):
        """
        @node:ast.AST
        """
        self.classes.append(node)
        
        clsWalker = ClassDefWalker(node, self.nameSpace, self.scope.copy())
        clsWalker.walk()
        
        self.nameSpace.put(clsWalker.name, clsWalker.createClassBean())
        
         
    def visit_FunctionDef(self, node):
        """
        @node:ast.AST
        """
        self.funs.append(node)

        funWalker = FunDefWalker(node, self.nameSpace, self.scope.copy())   
        funWalker.walk()
             
        self.nameSpace.put(funWalker.name, funWalker.createFunBean())
        
        print("out fun")
         

    def checkResults(self):
        for cla in self.classes:
            print(ast.dump(cla))
        for fun in self.funs:
            print(ast.dump(fun))
        for glob in self.globals:
            print(ast.dump(glob))
            
class ClassDefWalker(InitialWalker):
    
    def __init__(self, classRoot, nameSp, scopeCopy):
        """
        @classRoot:ast.ast
        @nameSp:bean.NameSpaceBean
        @scopeCopy:bean.ScopeBean
        """
        self.root = classRoot
        self.initFun = None
        self.nameSpace = nameSp
        self.funs = Bean.NameSpaceBean()
        self.selfVars = scopeCopy
        self.name = classRoot.name
       
    def walk(self):
        #first call should be a quick walk to snag all of the fun names and self var names
        self._first_visit(self.root)
        #second walk call should be to actually do the checking  
        self._second_visit(self.root)
        
    def _first_visit(self, node):
        """
        @node:ast.ast
        """
        #todo initial pass
        self.visit(node)
        
    def _second_visit(self, node):
        """
        @node:ast.ast
        """
        #todo full pass
        self.visit(node)
        
    def visit_FunctionDef(self, node):
        """
        @node:ast.ast
        """
        self.funs.append(node)
        if(node.name == '__init__'):
            self.initFun = node
    
    def createClassBean(self):
        bean = Bean.ClassDefBean(self.name, self.selfVars)
#         stuff about making the bean
        return bean
    
class FunDefWalker(InitialWalker):
    def __init__(self, funRoot, nameSp, scopeLevel):
        """
        @funRoot:ast.ast
        @nameSp:bean.NameSpaceBean
        @scopeLevel:bean.ScopeLevelBean
        """
        self.name = funRoot.name
        self.root = funRoot
        self.retType = None
        self.scope = scopeLevel
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
        
