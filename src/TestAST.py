'''
Created on Sep 19, 2014

@author: daviis01

This file is where the command line option parser should direct to for the heavy lifting of static analysis. It will also be used for testing.
'''
import ast
import Bean
from SecondWalkerAttempt import InitialWalker, ClassDefWalker, FunDefWalker

def main():
#    aFile = "../test/correct/add.py"
#    aFile = "../test/correct/AccPat.py"
#    aFile = "../test/incorrect/StrPlusInt.py"
#     aFile = "../test/correct/MultiClassMultiFun.py"
    aFile = "../Test/correct/SingleMethodDef.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()
    #parser.expr(fileCont, "aFile", 'eval')
    tree = ast.parse(fileCont, aFile)
    print ((ast.dump(tree)))
    
    nameSpace = Bean.NameSpaceBean()
    scope = Bean.ScopeLevelBean()
    
    firstWalker = InitialWalker(tree)
    firstWalker.walk()
    print("made firstwakler")
#     firstWalker.checkResults()
    
    
    #the interrupt work should be around here
    if not firstWalker.classes and not firstWalker.funs:
        print("no classes or functions")
        
    for aClass in firstWalker.classes:
        classWalker = ClassDefWalker(aClass, nameSpace, scope.copy())
        classWalker.walk()
        nameSpace.put(classWalker.name, classWalker.createClassBean())
        print("\none class")
#         classWalker.checkResults()
        
    for aFun in firstWalker.funs:
        funWalker = FunDefWalker(aFun, nameSpace, scope)
        funWalker.walk()
        nameSpace.put(funWalker.name, funWalker.createFunBean())
        print("\none fun")
#         funWalker.checkResults()
        
    print("out")

if __name__ == '__main__':
    main()
    print("out main")