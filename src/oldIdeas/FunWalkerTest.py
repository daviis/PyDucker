'''
Created on Oct 25, 2014

@author: daviis01

This class is to test how to make a fun bean from a funwalker.
'''
import Bean
from Walker import FunDefWalker, InitialWalker
import ast

def main():
    aFile = "../test/correct/MethodDef.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()
    tree = ast.parse(fileCont, aFile)
    firstWalker = InitialWalker(tree)
    for aFun in firstWalker.funs:
        funWalker = FunDefWalker(aFun, firstWalker.globals)
        
        funBean = funWalker.createFunBean()
        firstWalker.nameSpace.put(funBean.name, funBean)
    
    print("exiting")
        


if __name__ == '__main__':
    main()
    