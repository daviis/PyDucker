'''
Created on Oct 13, 2014

@author: daviis01
'''
import ast

class MyVisitor(ast.NodeVisitor):
    def __init__(self, astRoot):
        self.lineage = [astRoot]
        self.nextChildIndex = 0 
        self.currentNode = astRoot
        self._fillStack()

    def _fillStack(self):
        tempNode = self.currentNode.body[0]
        while tempNode:
            self.lineage.append(tempNode)
            self.currentNode = tempNode
            if hasattr(self.currentNode, 'body'):
                tempNode = self.currentNode.body[0]
            else:
                tempNode = None
            self.nextChildIndex = 1
            
    def _inorderTraversal(self):
        hasNextChild = self.nextChildIndex < len(self.lineage[-1].body) 
        if hasNextChild:
            self.currentNode = self.lineage[-1].body[self.nextChildIndex]
            self.nextChildIndex += 1
            return True
        else:
            if len(self.lineage) >= 0:
                self.currentNode = self.lineage.pop()
                self.nextChildIndex = 1
                self._fillStack()
                return True
            else:
                return False
                
    def getChild(self):
        return self._inorderTraversal()