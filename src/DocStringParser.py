'''
Created: 2014/10/14
Updated: 2014/11/12
@author: Jake Albee
'''
import re
from Bean import VarBean
from Bean import ScopeLevelBean
import Exceptions

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
                    raise Exceptions.HeteroCollecionException(variables,-1)
                elif currentType == '^':
                    raise Exceptions.HeteroCollecionException(variables,-1)
                elif currentType == '**':
                    raise Exceptions.HeteroCollecionException(variables,-1)
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
                    compType, valueType = currentType[:-2].split(':')
                    #List is [key,value]
                    mainVarType = 'dict'
                elif currentType[1] == '*':
                    compType, valueType = currentType[2:].split(':')
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
            mainVarType = currentType

        for key in variables:
            currentVar = VarBean(mainVarType, key)
            if isHomo == False:
                currentVar.homo = False
            else:
                if len(compType) < 2:
                    currentVar.homo = True
                else:
                    currentVar.homo = True
                    #Handle dict here, not sure how to set keys or values
                    currentVar.compType = [VarBean(compType)]
                    if mainVarType == "dict":
                        currentVar.valType = [VarBean(valueType)]
            finalList.append(currentVar)
    
    if returnList == False:
        return ScopeLevelBean(finalList)
    else:
        return finalList
