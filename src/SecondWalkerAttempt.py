'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast
import Bean
from DocStringParser import parseDocString

class InitialWalker(ast.NodeVisitor):
    def __init__(self, astNode):
        """
        #! astNode:ast.AST
        """
        self.root = astNode
        self.classes = []
        self.funs = []
        self.globals = []
        self.nameSpace = Bean.NameSpaceBean()
        
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
    iterate over it. If not, then a single generic_visit is needed
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
            
    def visit_AugAssign(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
           
    def visit_BinOp(self, node):
        leftType = self.visit(node.left)
        op = self.visit(node.op)
        right = self.visit(node.right)
        #look up if the method is contained in the left, if not then maybe the right
        #if so, then return the return type of the function 
        return "some type from binop"
         
    def visit_Call(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
 
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
        #! node:ast.AST
        """
        self.nameSpace.put(node.name)
        self.classes.append(node)
         
    def visit_FunctionDef(self, node):
        """
        #! node:ast.AST
        """
        self.nameSpace.put(node.name)
        self.funs.append(node)
         

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
        print(self.retType)
        
