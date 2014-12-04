'''
Created on Sep 19, 2014

@author: daviis01

This file is where the command line option parser should direct to for the heavy lifting of static analysis. It will also be used for testing.
'''
import ast
import Bean
from Walker import InitialWalker
from NameSpaceBeans import handMakeNameSpace

def main():
    #open a file and get it read into a variable so it is just one string
    aFile = "../Test/correct/StoreLoad.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()

    #parse the string into an ast using the builtin function
    tree = ast.parse(fileCont, aFile)
    print ((ast.dump(tree)))
    
    #make some 
#     nameSpace = Bean.NameSpaceBean()
    nameSpace = handMakeNameSpace()
    scope = Bean.ScopeLevelBean()
    
#     firstWalker = InitialWalker(tree, nameSpace, scope)
    firstWalker = InitialWalker(tree, nameSpace, scope)
    firstWalker.walk()
#     firstWalker.checkResults()

    #do some exception handling that will tell the user what went wrong in their project

if __name__ == '__main__':
    main()
    print("out main")