'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast
import bean

class InitialWalker(ast.NodeVisitor):
    def __init__(self, astNode):
        """
        #! astNode:ast.AST
        """
        self.root = astNode
        self.classes = []
        self.funs = []
        self.globals = []
        self._initalPass()
        
    def _initalPass(self):
        self.generic_visit(self.root)
        
#     def generic_visit(self, node):
#         """
#         This function is to identify what type of visits should be made. 
#         The type(node).__name__ returns the word to append to visit_ 
#         to make a visitor
#         """
#         print (type(node).__name__)
#         ast.NodeVisitor.generic_visit(self, node)
         
    def visit_ClassDef(self, node):
        """
        #! node:ast.AST
        """
        self.classes.append(node)
        
    def visit_FunctionDef(self, node):
        """
        #! node:ast.AST
        """
        self.funs.append(node)
        
    def visit_Assign(self, node):
        self.globals.append(node)
        
    def checkResults(self):
        for cla in self.classes:
            print(ast.dump(cla))
        for fun in self.funs:
            print(ast.dump(fun))
        for glob in self.globals:
            print(ast.dump(glob))
            
class ClassDefWalker(InitialWalker):
    
    def __init__(self, classRoot):
        """
        @classRoot:ast.ast
        """
        self.root = classRoot
        self.initFun = None
        self.funs = []
        self.name = classRoot.name
        self.generic_visit(self.root)
        
    def visit_FunctionDef(self, node):
        """
        @node:ast.ast
        """
        self.funs.append(node)
        if(node.name == '__init__'):
            self.initFun = node
    
    def createClassBean(self):
        bean = bean.ClassBean
#         stuff about making the bean
        return bean
    
class FunDefWalker(InitialWalker):
    def __init__(self, funRoot, scopeLevel):
        """
        @funRoot:ast.ast
        @scopeLevel:bean.LevelBean
        """
        self.name = funRoot.name
        self.root = funRoot
        self.retType = None
        self.scope = scopeLevel
    
    def createFunBean(self):
        bean = bean.FunDefBean
#         stuff about making the bean
        return bean
