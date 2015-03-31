'''
Created: 2014/10/14
Updated: 2014/11/12
@author: Jake Albee
'''
import re
import sys
from Bean import VarBean
from Bean import ScopeLevelBean

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
        current = current.split(':',maxsplit=1)
        variables = current[0].split(',')
        currentType = current[1]
        
        compType = None
        if re.search(matchPattern,currentType):
            if len(currentType) <= 2:
                isHomo = False
                if currentType == '*':
                    print('**Warning** List(s) '+str(variables)+ ' are inhomogeneous.',file=sys.stderr)
                    mainVarType = 'list'
                elif currentType == '^':
                    print('**Warning** Tuple(s) '+str(variables)+ ' are unknown.',file=sys.stderr)
                    mainVarType = 'tuple'
                elif currentType == '**':
                    print("**Warning** Dictionary(s) "+str(variables)+ ' are inhomogeneous.',file=sys.stderr)
                    mainVarType = 'dict'
            else:
                isHomo = True
                #We'll handle Tuples first.
                if currentType[0] == '^':
                    compType = currentType[1:]
                    mainVarType = 'tuple'
                elif currentType[-1] == '^':
                    compType = currentType[:-1]
                    mainVarType = 'tuple'
                #Tuple handled.
                elif currentType[-2] == '*':
                    compType = currentType[:-2].split(':')
                    mainVarType = 'dict'
                elif currentType[1] == '*':
                    compType = currentType[2:].split(':')
                    mainVarType = 'dict'
                #Dicts handled
                elif currentType[0] == '*':
                    compType = currentType[1:]
                    mainVarType = 'list'
                elif currentType[-1] == '*':
                    compType = currentType[:-1]
                    mainVarType = 'list'
                #lists handled
        else:
            isHomo = False

        for key in variables:
            currentVar = VarBean(mainVarType, key)
            if isHomo == False:
                currentVar.homo = False
            else:
                if compType:
                    currentVar.homo = True
                    currentVar.compType = [VarBean(compType)]
            finalList.append(currentVar)
    
    if returnList == False:
        return ScopeLevelBean(finalList)
    else:
        return finalList
    
