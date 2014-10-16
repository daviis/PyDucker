'''
Created on Sep 19, 2014

@author: daviis01
'''
import ast
  
from SecondWalkerAttempt import Walker
        

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
    aWalker = Walker(tree)
    print("made wakler")
    aWalker.checkResults()

if __name__ == '__main__':
    main()
    print("out")