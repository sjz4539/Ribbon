'''
Created on Feb 18, 2017

@author: Steven Zuchowski
'''

from Node import Node
from LinkedList import LinkedList
from datetime import datetime
from ribbon.TimeslotView import TimeslotView

class Timeslot(Node, LinkedList):
    '''
    classdocs
    '''

    def __init__(self, time=datetime.now()):
        super().__init__()
        self.time = time
        
    
    def getView(self, parent):
        return TimeslotView(parent, self)
