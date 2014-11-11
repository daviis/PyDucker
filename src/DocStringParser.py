'''
Created: 10/14/14
Updated: 10/30/14
@author: Jake Albee
'''
import re
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
    listWarn = '**WARNING** Lists can be of unknown types! '
    dictWarn = '**WARNING** Dictionaries can be of unknown types! '
    matchPattern = '\*\*?.*|.*\*\*?'
    for i in lineList:
        current = i[1:] #Remove the @
        current = current.replace(" ","") #Remove all spaces for easier parsing
        current = current.split(':')
        variables = current[0].split(',')
        currentType = current[1]
        
        if re.search(matchPattern,currentType):
            if currentType[1] == '*':
                currentType= dictWarn +  currentType
            elif currentType[0] == '*':
                currentType= listWarn +  currentType
            elif currentType[-2] == '*':
                currentType= dictWarn +  currentType
            elif currentType[-1] == '*':
                currentType= listWarn +  currentType
                
        for key in variables:
            finalList.append(VarBean(key,currentType))
            
    if returnList == False:
        return ScopeLevelBean(finalList)
    else:
        return finalList
    
