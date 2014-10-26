'''
Created on Sep 19, 2014

@author: daviis01

This file is where the command line option parser should direct to for the heavy lifting of static analysis. It will also be used for testing.
'''
import ast
  
from SecondWalkerAttempt import InitialWalker, ClassDefWalker, FunDefWalker
        

def main():
#    aFile = "../test/correct/add.py"
#    aFile = "../test/correct/AccPat.py"
#    aFile = "../test/incorrect/StrPlusInt.py"
    aFile = "../test/correct/MultiClassMultiFun.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()
    #parser.expr(fileCont, "aFile", 'eval')
    tree = ast.parse(fileCont, aFile)
    print ((ast.dump(tree)))
    firstWalker = InitialWalker(tree)
    print("made firstwakler")
#     firstWalker.checkResults()
    
#     nameSpace = LevelBean()
    
    #the interrupt work should be around here
    if not firstWalker.classes and not firstWalker.funs:
        funWalker = FunDefWalker(tree)
        print("no classes or functions")
        funWalker.checkResults()
        
    for aClass in firstWalker.classes:
        classWalker = ClassDefWalker(aClass)
        firstWalker.nameSpace.put(classWalker.name, classWalker.createClassBean())
        print("\none class")
#         classWalker.checkResults()
        
    for aFun in firstWalker.funs:
        funWalker = FunDefWalker(aFun, firstWalker.nameSpace)
        firstWalker.nameSpace.put(funWalker.name, funWalker.createFunBean())
        print("\none fun")
#         funWalker.checkResults()
        
    print("out")

if __name__ == '__main__':
    main()
    print("out")