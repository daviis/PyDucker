'''
Created on Sep 19, 2014

@author: daviis01
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
        print("\none class")
#         classWalker.checkResults()
    for aFun in firstWalker.funs:
        funWalker = ClassDefWalker(aFun)
        print("\none fun")
        funWalker.checkResults()

if __name__ == '__main__':
    main()
    print("out")