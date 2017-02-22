'''
Created on Feb 18, 2017

@author: Test
'''

class Node(object):
    '''
    classdocs
    '''

    def __init__(self, prevNode=None, nextNode=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        
    
    def insertBehind(self, node):
        if not self.nextNode is None:
            self.nextNode.prevNode = node
            
        node.nextNode = self.nextNode
        self.nextNode = node
        node.prevNode = self
        
        
    def insertBefore(self, node):
        if not self.prevNode is None:
            self.prevNode.nextNode = node
            
        node.prevNode = self.prevNode
        self.prevNode = node
        node.nextNode = self
        
        
    def removeSelf(self):
        if not self.prevNode is None:
            self.prevNode.nextNode = self.nextNode
            
        if not self.nextNode is None:
            self.nextNode.prevNode = self.prevNode
