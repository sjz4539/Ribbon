'''
Created on Feb 20, 2017

@author: Test
'''
from tkinter import LabelFrame

class TimeslotView(LabelFrame):
    
    def __init__(self, parent, timeslot):
        super().__init__(parent)
        self.timeslot = timeslot
        self.configure(text=str(timeslot.time))
        self.onModelChanged()
    
    
    def removeAll(self):
        for reminder in self.timeslot:
            reminder.destroyView(self)
    
    
    def destroyView(self):
        self.removeAll()
        self.destroy()
        
    
    def onModelChanged(self):
        self.removeAll()
        for reminder in self.timeslot:
            reminder.getView(self).pack(side="top")