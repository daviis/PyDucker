'''
Created on Nov 17, 2014

@author: daviis01
'''
import ast
from SecondWalkerAttempt import InitialWalker, ClassDefWalker, FunDefWalker
from Bean import VarBean
        
class TestWalker(InitialWalker):
    
    def __init__(self, node):
        self.head = node
        
    def walk(self):
        self.generic_visit(self.head)
        
    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        if isinstance(node, list):
            for item in node:
                if isinstance(item, ast.AST):
                    return self.visit(item)
        elif isinstance(node, ast.AST):
            return self.visit(node)
        
    def visit_BinOp(self, node):
        types = []
        for field, value in ast.iter_fields(node):
            types.append(self.generic_visit(value))
        print(types)
        

    def visit_Module(self, node):
        for _, value in ast.iter_fields(node):
            self.generic_visit(value)
            
    def visit_Expr(self, node):
        for _, value in ast.iter_fields(node):
            self.generic_visit(value)
            
    def visit_Add(self, node):
        return "__add__"
            
    def visit_Num(self, node):
        return "int"
    
    def visit_Str(self, node):
        return "str"
        
def main():
    fileContents = "5+'a'"
    tree = ast.parse(fileContents)
    print ((ast.dump(tree)))
    
    walker = TestWalker(tree)
    walker.walk()
    
    
    
if __name__ == '__main__':
    main()  