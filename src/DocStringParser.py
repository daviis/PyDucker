'''
Created: 10/14/14
Updated: 10/27/14
@author: Jake Albee
'''
import re
from src.Bean import VarBean
#from src.Bean import LevelBean

def parseDocString(docString,returnList = True):
    """Takes in a doc string in the form of a string and returns a list of VarBeans
    or a ScopeLevelBean. Defaults to returning a list of VarBeans
    @docString:string
    """
    lineList = docString.splitlines()
    for i in lineList:
        if not re.match('@.+', i, flags=0):
            lineList.remove(i)
    finalList = []
    for i in lineList:
        current = i[1:] #Remove the @
        current = current.replace(" ","") #Remove all spaces for easier parsing
        current = current.split(':')
        variables = current[0].split(',')
        currentType = current[1]
        if currentType[0] == '*':
            currentType='**WARNING** Lists can be of unknown types!' +  currentType
        elif currentType[1] == '*':
            currentType='**WARNING** Dictionaries can be of unknown types!' +  currentType
        print(currentType)
        for key in variables:
            newBean = VarBean(key,currentType)
            finalList.append(newBean)
            
            
    if returnList == True:
        return finalList
    else:
        #Returning a ScopeLevelBean
        return finalList
