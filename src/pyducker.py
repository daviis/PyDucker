'''
Created on Sep 18, 2014

@author: daviis01
'''
import sys
import ast
import argparse

import Bean
import Exceptions
from Walker import InitialWalker
from NameSpaceBeans import handMakeNameSpace, handMakeScope


def testFiles(listOfFiles, PyduckerWarningOff):
    for i in listOfFiles:
        aFile = i.name
        
        with open(aFile, 'r') as f:
            fileCont = f.read()
            
        print("File name: ",aFile)
        try: 
            tree = ast.parse(fileCont, aFile)
            
        #except ast.parser.ParseError:
         #   print('hit')
        except BaseException:
            type, value, tb = sys.exc_info()
            print("Unable to parser file due to" ,type.__name__) 
            print(  type.__name__, ":"  , value)
            
            tree = None
        if PyduckerWarningOff:
            try:
                nameSpace = handMakeNameSpace()
                scope = handMakeScope()
                firstWalker = InitialWalker(tree, nameSpace, scope)
                firstWalker.walk()
      
            except Exceptions.PyDuckerError as ex:
                print("\n", ex.__class__.__name__, end = "")
                print(ex)
            except Exceptions.PyDuckerWarning as ex:
                pass
            finally:
                print()
        else:        
            try:
                nameSpace = handMakeNameSpace()
                scope = handMakeScope()
                firstWalker = InitialWalker(tree, nameSpace, scope)
                firstWalker.walk()
      
            except Exceptions.PyDuckerException as ex:
                print("\n", ex.__class__.__name__, end = "")
                print(ex)
            finally:
                print()

def main():
    parser = argparse.ArgumentParser(description="A static analysis tool for Python 3.x")
    parser.add_argument('files', metavar='F', type=open, nargs='+',
                   help='an file to statically check')
    parser.add_argument('-n', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='check the variable names in the file only')
    parser.add_argument('-w', action='store_const', const = 'false', help = 'turns of PyDucker warnings')
    args = parser.parse_args()
    
    if args.files:
        testFiles(args.files, args.w) #args.w well tell if PyDuckerWarning should be on or off
    



if __name__ == '__main__':
    main()