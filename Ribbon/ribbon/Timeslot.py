'''
Created on Feb 18, 2017

@author: Steven Zuchowski
'''

from Node import Node
from LinkedList import LinkedList
from TimeslotView import TimeslotView

class Timeslot(LinkedList, Node):
    '''
    classdocs
    '''

    def __init__(self, time):
        LinkedList.__init__(self)
        Node.__init__(self)
        
        self.views = {}
        
        self.time = time
        
        
    def getView(self, parent):
        if parent not in self.views:
            self.views[parent] = TimeslotView(parent, self)
            
        return self.views[parent]
    
    
    def destroyView(self, parent):
        if parent in self.views:
            self.views[parent].destroy()
            del self.views[parent]