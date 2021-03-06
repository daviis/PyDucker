'''
Created on Sep 19, 2014

@author: daviis01

This file is where the command line option parser should direct to for the heavy lifting of static analysis. It will also be used for testing.
'''
import ast


import Exceptions
from Walker import InitialWalker
from NameSpaceBeans import handMakeNameSpace, handMakeScope

def testOne(aFile):
    """
    @aFile:str
    """
    #open a file and get it read into a variable so it is just one string
    print("Reading file ", aFile)
    with open(aFile, 'r') as f:
        fileCont = f.read()

    #parse the string into an ast using the builtin function
    tree = ast.parse(fileCont, aFile)
    print ((ast.dump(tree)))
    nameSpace = handMakeNameSpace()
    scope = handMakeScope()
    
    firstWalker = InitialWalker(tree, nameSpace, scope)
    firstWalker.walk()
    print("")

    #do some exception handling that will tell the user what went wrong in their project
def testAllCorrect():
    #Non-working tests are commented out    
    files = [
            '../Test/Correct/Call.py',
            '../Test/Correct/classes.py',
            '../Test/Correct/Collections.py',
            '../Test/Correct/control.py',
            '../Test/Correct/MethodDef.py',
            '../Test/Correct/MultiClassMultiFun.py',
            '../Test/Correct/NonlocalGlobal.py',
            '../Test/Correct/Ops.py',
            '../Test/Correct/ScopeLevels.py',
            '../Test/Correct/simpleSuper.py',
            '../Test/Correct/SingleClass.py',
            '../Test/Correct/slice.py',
            '../Test/Correct/tryRaiseExcept.py',
            '../Test/Correct/With.py',
            '../Test/Correct/Yield.py',
             ]
    _testAll(files)
    
    
def testAllIncorrect():
    files = ['../Test/Incorrect/BinOp.py',
             '../Test/Incorrect/Call.py',
#              '../Test/Incorrect/ClassBiReference.py',
             '../Test/Incorrect/Compare.py',
             '../Test/Incorrect/generalTest.py',
#              '../Test/Incorrect/localFun.py',
#              '../Test/Incorrect/ScopeTest.py',
             '../Test/Incorrect/StrPlusInt.py',
             '../Test/Incorrect/Yield.py'
             ]
    
    _testAll(files)
    
def _testAll(listOfFiles):
    for i in listOfFiles:
        aFile = i
        #print("Reading file ", aFile)
        with open(aFile, 'r') as f:
            fileCont = f.read()
            
        print("File name: ",aFile) 
        tree = ast.parse(fileCont, aFile)
        print("Tree Dump: ",ast.dump(tree))

        try:
            nameSpace = handMakeNameSpace()
            scope = handMakeScope()
            firstWalker = InitialWalker(tree, nameSpace, scope)
            firstWalker.walk()
        except Exceptions.PyDuckerException as ex:
#             print(ex, file=sys.stderr) #printing to sys.stderr will need to be locked so output flows correctly, otherwise the messages come out interwoven.
            print("\n", ex.__class__.__name__, end= "" )
            print(ex)
        finally:
            print()
            

    
if __name__ == '__main__':
    testOne("../Test/Incorrect/LocalFun.py")
#     testAllCorrect()
    #testAllIncorrect()
    print("out main")
