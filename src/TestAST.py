'''
Created on Sep 19, 2014

@author: daviis01
'''
import ast

def main():
#    aFile = "../test/correct/add.py"
#    aFile = "../test/correct/AccPat.py"
    aFile = "../test/incorrect/StrPlusInt.py"
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()
    #parser.expr(fileCont, "aFile", 'eval')
    tree = ast.parse(fileCont, aFile)
    print (ast.dump(tree))

if __name__ == '__main__':
    main()
    print("out")