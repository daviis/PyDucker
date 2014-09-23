#Jake Albee
#import parser
import ast

file = '../test/generalTest.py'

def testInts():
    x = 1
    y = x+x
    print(y)
    
    
class FuncLister(ast.NodeVisitor):
    """
    This class lists the different function names
    """
    def visit_FunctionDef(self, node): #Override visit_nodeType
        print(node.name) #Print the name of def since it requires a name
        #=======================================================================
        # This would print the docstring of the node 
        # print(ast.get_docstring(node))
        #=======================================================================
        self.generic_visit(node) #Visit all the children nodes
        
        
class VariableLister(ast.NodeVisitor):
    """
    This class lists the different variable names
    """
    def visit_Assign(self, node): #Override visit_nodeType
        self.generic_visit(node) #Visit all the children nodes
        childrenNodes = ast.iter_child_nodes(node) #Build an interator over the children of current node
        for childNode in childrenNodes: #Iterate over the children of the node
            if isinstance(childNode, ast.Name): #If the node is an instance of the AST's Name nodes
                print(childNode.id) #Print the child node's id
        
        
def main():
    """
    Testing reading capabilities
    """ #Define the file
    x = open(file, mode='r') #Open the file
    string = '' #AST reads strings
    
    for i in x:
        string+=i
        #Build the string to use
    tree = ast.parse(string) #Parse the string into an AST
    print('The code in the file: \n\n'+string+'\n')
    print('=======================================\n')
    print('The AST: '+ast.dump(tree)) #Readable dump of tree
    print('=========================================\n')
    print('Variables: \n')
    VariableLister().visit(tree)
    print()
    print('Functions: \n')
    FuncLister().visit(tree)
    print()
    
    #===========================================================================
    # To actually edit the nodes you have to use
    # ast.NodeTransformer
    #===========================================================================
            
    
        
main()
    