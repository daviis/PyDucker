'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast

class Walker(ast.NodeVisitor):
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
#         print (type(node).__name__)
#         ast.NodeVisitor.generic_visit(self, node)
#         
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
        
    def checkResults(self):
        for cla in self.classes:
            print(ast.dump(cla))
        for fun in self.funs:
            print(ast.dump(fun))
        for glob in self.globals:
            print(ast.dump(glob))