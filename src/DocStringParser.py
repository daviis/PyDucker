'''
Created: 10/14/14
Updated: 10/30/14
@author: Jake Albee
'''
import re
import sys
from src.Bean import VarBean
from src.Bean import ScopeLevelBean


def parseDocString(docString,returnList = True):
    """Takes in a doc string in the form of a string and returns a list of VarBeans
    or a ScopeLevelBean. Defaults to returning a list of VarBeans
    @docString:string
    @returnList:bool
    """
    lineList = docString.splitlines()
    for i in lineList:
        if not re.match('@.+', i, flags=0):
            lineList.remove(i)
    finalList = []
    matchPattern = '\*\*?.*|.*\*\*?|\^.*|.*\^'
    for i in lineList:
        current = i[1:] #Remove the @
        current = current.replace(" ","") #Remove all spaces for easier parsing
        current = current.split(':')
        variables = current[0].split(',')
        currentType = current[1]
        #
        #TODO print to std.err for error messages
        #manage non-homo
        #deal with this crap
        #
        compType = None
        if re.search(matchPattern,currentType):
            isHomo = checkIfHomo(currentType)
            if len(currentType) <= 2:
                if currentType == '*':
                    print('**Warning** List(s) '+str(variables)+ ' are inhomogeneous.',file=sys.stderr)
                elif currentType == '^':
                    print('**Warning** Tuple(s) '+str(variables)+ ' are unknown.',file=sys.stderr)
                elif currentType == '**':
                    print("**Warning** Dictionary(s) "+str(variables)+ ' are inhomogeneous.',file=sys.stderr)
            else:
                #do lots of stuff here
                pass
                    
        #Handled: inhomogeneous lists,tuples,dictionaries that have no typing informatin
        #Lots to do here
        #Need to get the */**/^ off the string and then check that for a split if a dict
        #For tuples the comp type will be..?
        #
                
        if currentType[1] == '*':
            currentType= dictWarn +  currentType
        elif currentType[0] == '*':
            currentType= listWarn +  currentType
        elif currentType[-2] == '*':
            currentType= dictWarn +  currentType
        elif currentType[-1] == '*':
            currentType= listWarn +  currentType
        elif currentType[-1] == '^':
            print('found carat')
        elif currentType[0] == '^':
            print('found carat')
                
        
        for key in variables:
            currentVar = VarBean(key,currentType)
            if isHomo == False:
                currentVar.homo = False
            else:
                if compType:
                    currentVar.compType = compType
            finalList.append(currentVar)
                
            
    if returnList == False:
        return ScopeLevelBean(finalList)
    else:
        return finalList
    
def checkIfHomo(string):
    '''@string:string
    '''
    if len(string)>1:
        return True
    else:
        return False
    
    
parseDocString('@string:^')
