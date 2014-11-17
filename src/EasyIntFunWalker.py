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
        
    def visit_BinOp(self, node):
        leftType = self.generic_visit(node.left)
        rightType = self.generic_visit(node.right)
        op = node.op.__class__.__name__
        print(op)
        
    def visit_Num(self, node):
        return "int"
        
def main():
    fileContents = "1+2"
    tree = ast.parse(fileContents)
    print ((ast.dump(tree)))
    
    walker = TestWalker(tree)
    walker.walk()
    
    
    
if __name__ == '__main__':
    main()  