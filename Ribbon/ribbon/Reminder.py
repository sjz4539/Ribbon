'''
Created on Feb 18, 2017

@author: Steven Zuchowski
'''

from Node import Node
from ReminderView import ReminderView

class Reminder(Node):
    '''
    classdocs
    '''
    
    def __init__(self, when, title=None, message=None):
        super().__init__(self)
        
        self.views = {}
        
        self.when = when
        self.title = title if not title is None else ""
        self.message = message if not message is None else ""
        
        
    def getView(self, parent):
        if parent not in self.views:
            self.views[parent] = ReminderView(parent, self)
            
        return self.views[parent]
    
    
    def destroyView(self, parent):
        if parent in self.views:
            self.views[parent].destroy()
            del self.views[parent]