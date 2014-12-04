'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast
import Bean
from DocStringParser import parseDocString
import sys

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
            return self.visit(node)
        #set a break point on this to find where there is a need to list-ify a vist_
        elif isinstance(node, list):
            print('got a list')
         
         
    """
    Each individual vist_* will need to check if the result if a list, if so then 
    iterate over it. If not, then a single visit is needed
    """
    def visit_Add(self, node):
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
           
    def visit_BinOp(self, node):
        """
        This will return either a single type or a list of two types that it could be
        @node:ast.node
        """
        leftType = self.visit(node.left)
        op = self.visit(node.op)
        rOp = op[:2] + 'r' + op[2:]
        rightType = self.visit(node.right)
        #look up if the method is contained in the left, if not then maybe the right
        #if so, then return the return type of the function
        
        leftBean = self.nameSpace[leftType]
        rightBean = self.nameSpace[rightType]
        
        if leftBean.hasMethod(op):
            if leftBean[op].takes([rightType]):
                return leftBean[op].retType
        if rightBean.hasMethod(rOp):
            if rightBean[rOp].takes([leftType]):
                return rightBean[rOp].retType
        else:
            print('Error found when trying to '+ op + 'on ' + leftType +', ' + rightType +'.',sys.stderr)

        return "some type from binop"
         
    def visit_Call(self, node):
        """
        Fields are ('func', 'args', 'keywords', 'starargs', 'kwargs')
        @node:ast.ast
        """
        cls, funcName = self.visit(node.func)
        args = self.visit(node.args)
        keywords = self.visit(node.keywords)
        starargs = self.visit(node.starargs)
        kwargs = self.visit(node.kwargs)
        
        clsBean = self.nameSpace[cls]
        if clsBean.hasFun(funcName):
            #fundefbean will need to be extended to handle things other than just a fixed lenght number of params
            if clsBean[funcName].takes(args):
                return clsBean[funcName].returnType
        else:
            print("class: " + clsBean.name + " doesn't have method: " + funcName, sys.stderr)
 
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
        for _, value in ast.iter_fields(node):
            self.visit(value)

    def visit_Mult(self, node):
        return "__mul__"
    
    def visit_Name(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
             
    def visit_Num(self, node):
        return type(node.n).__name__
     
    def visit_Return(self, node):
        #may need to look at the other fields in ast.Return but the basic way is this. 
        val = self.visit(node.value)
            
    def visit_Store(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
            
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
        
