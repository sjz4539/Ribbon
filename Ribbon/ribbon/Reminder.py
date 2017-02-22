'''
Created on Feb 18, 2017

@author: Steven Zuchowski
'''

from Node import Node
from ribbon.ReminderView import ReminderView

class Reminder(Node):
    '''
    classdocs
    '''
    
    def __init__(self, title=None, message=None):
        super().__init__()
        self.title = title if not title is None else ""
        self.message = message if not message is None else ""
        self.triggered = False
    
        
    def setTriggered(self, trig):
        self.triggered = trig
        
        
    def getView(self, parent):
        return ReminderView(parent)