'''
Primary GUI class.
GUI interaction from other modules should be performed through this class only.

Created on Feb 20, 2017

@author: Test
'''

from tkinter import Frame, Button, Tk
from DayView import DayView
from DateChooser import DateChooser
from ReminderDialog import ReminderDialog
import Ribbon

class Gui(Tk):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.dateChooser = DateChooser(self)
        self.rightFrame = Frame(self)
        self.newReminderButton = Button(self.rightFrame, text="Add Reminder", command=lambda: self.wait_window(ReminderDialog(self)))
        self.dayView = DayView(self.rightFrame)
        
        self.dateChooser.setOnDateSelected(Ribbon.setSelectedDate)
        
        self.dateChooser.pack(side="left", fill="both")
        self.dayView.pack(side="top", fill="both")
        self.newReminderButton.pack(side="bottom", fill="x")
        self.rightFrame.pack(side="right", fill="both")
        
     
    def refreshReminderList(self):
        self.dayView.onContentsChanged()
        
        
    def showDate(self, year, month, day):
        self.dayView.showDate(year, month, day)
        
        
    def showReminderDialog(self, reminder=None):
        self.wait_window(ReminderDialog(self, reminder))
        