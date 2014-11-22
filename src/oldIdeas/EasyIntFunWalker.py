'''
Created on Nov 17, 2014

@author: daviis01

This file is for testing some walker framework stuff. 

update: 2014-11-19
It looks like recursively walking the tree will work. 
'''
import ast
from Walker import InitialWalker, ClassDefWalker, FunDefWalker
from Bean import VarBean
        
class TestWalker(InitialWalker):
    
    def __init__(self, node):
        self.head = node
        
    def walk(self):
        self.visit(self.head)
        
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
            
    def visit_FunctionDef(self, node):
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
        return "int"
     
    def visit_Return(self, node):
        #may need to look at the other fields in ast.Return but the basic way is this. 
        val = self.visit(node.value)
        print(val)
            
    def visit_Store(self, node):
        for _, value in ast.iter_fields(node):
            self.visit(value)
            
    def visit_Str(self, node):
        return "str"
     



            
        
def main():
    fileCont = "12*5.0"
    
    aFile = "../Test/correct/MultiClassMultiFun.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()
    
    tree = ast.parse(fileCont)
    print ((ast.dump(tree)))
    
    walker = TestWalker(tree)
    walker.walk()
    
    
    
if __name__ == '__main__':
    main()  