'''
Created on Feb 19, 2017

@author: Test
'''

class LinkedList(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        
    
    def append(self, node, after=None):
        if not after is None: # insert after target node
            
            # bump next node out of "next" slot if necessary
            if after.nextNode is self.next:
                self.next = node
            
            # update tail if necessary
            if self.tail is after:
                self.tail = node
            
            # insert new node
            after.insertBehind(node)
            
        else:
            if self.head is None:
                # insert as list head/tail/next
                self.head = node
                self.tail = node
                self.next = node
                
            else:
                # insert after list tail
                self.tail.insertBehind(node)
                
                # update "next" slot if necessary
                if self.next is None:
                    self.next = node
                
                # update tail
                self.tail = node


    def insert(self, node, before=None):
        if not before is None: # insert before target node
            
            # bump target node out of "next" slot if necessary
            if self.next is before:
                self.next = node
            
            # update head if necessary
            if self.head is before:
                self.head = node
            
            # insert new node
            before.insertBefore(node)
            
        else:
            if self.head is None:
                # insert as list head/tail/next
                self.head = node
                self.tail = node
                self.next = node
                
            else:
                # insert before list head
                self.head.insertBefore(node)
                
                # update "next" slot if necessary
                if self.head is self.next:
                    self.next = node
                
                # update tail
                self.head = node
        

    def appendAll(self, linkedlist):
        cur = linkedlist.head
        
        while not cur is None:
            self.append(cur)
            cur = cur.nextNode
            
    
    def remove(self, node):
        cur = self.head
        
        # iterate through the list until we find our 
        # target or hit the end of the list
        while not cur is None:
            if cur is node:

                # update our tracking pointers
                if cur is self.head:
                    self.head = cur.nextNode
                    
                if cur is self.tail:
                    self.tail = cur.prevNode

                if cur is self.next:
                    self.next = cur.nextNode
                    
                # remove the target node
                cur.removeSelf()
                    
                break
            
            else:
                cur = cur.nextNode
                
                
    def getNext(self):
        ret = self.next
        
        if not ret is None:
            self.next = ret.nextNode
            
        return ret
    
    