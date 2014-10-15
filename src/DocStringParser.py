'''
Created on Oct 14, 2014

@author: Jake Albee
'''
import re
def parseDocString(self,docString):
    """Takes in a doc string and prints out the types found inside it
    Returns a dictionary with key being the variable name, values being the type
    @docString:string
    @lineList,finalList:list
    """
    lineList = docString.splitlines()
    for i in lineList:
        if not re.match('@.+', i, flags=0):
            lineList.remove(i)
    finalList = {}
    for i in lineList:
        current = i[1:] #remove the @
        current = current.split(':')
        variables = current[0].split(',')
        currentType = current[1]
        #print(current[0].split(','))
        for key in variables:
            finalList[key] = currentType
    return finalList