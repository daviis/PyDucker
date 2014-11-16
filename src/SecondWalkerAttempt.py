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
        @astNode:ast.AST
        """
        self.root = astNode
        self.classes = []
        self.funs = []
        self.globals = []
        self.nameSpace = Bean.NameSpaceBean()
        
    def walk(self):
        self._first_visit()
        
    def _first_visit(self):
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
        @node:ast.AST
        """
        self.nameSpace.put(node.name)
        self.classes.append(node)
        
    def visit_FunctionDef(self, node):
        """
        @node:ast.AST
        """
        self.nameSpace.put(node.name)
        self.funs.append(node)
        
    def visit_Assign(self, node):
        #need to add global vars to namespace
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
        self.funs = Bean.NameSpaceBean()
        self.selfVars = Bean.ScopeLevelBean()
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
        self.generic_visit(node)
        
    def _second_visit(self, node):
        """
        @node:ast.ast
        """
        #todo full pass
        self.generic_visit(node)
        
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
    def __init__(self, funRoot, scopeLevel):
        """
        @funRoot:ast.ast
        @scopeLevel:bean.ScopeLevelBean
        """
        self.name = funRoot.name
        self.root = funRoot
        self.retType = None
        self.scope = scopeLevel
        
    def walk(self):
        pass
        
    def _findParamTypes(self):
        scopeObject = parseDocString(ast.get_docstring(self.root))
    
    def createFunBean(self):
        bean = Bean.FunDefBean(list(self.scope), self.retType, self.name)
#         stuff about making the bean
        return bean
