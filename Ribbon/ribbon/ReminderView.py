'''
Created on Feb 20, 2017

@author: Test
'''
from tkinter import Frame, Button, Label
import Ribbon

class ReminderView(Frame):
    '''
    classdocs
    '''

    def __init__(self, parent, reminder):
        super().__init__(parent)
        self.reminder = reminder
        self.config(background="blue")
        
        # we need:
        #    Title
        #    Alert Message
        #    Edit, Delete buttons
        
        self.labelFrame = Frame(self, bg="white")
        self.title = Label(self.labelFrame)
        self.message = Label(self.labelFrame)
        
        self.buttonFrame = Frame(self, bg="red")
        self.editButton = Button(self.buttonFrame, text="Edit", command=lambda reminder=self.reminder: Ribbon.editReminder(reminder))
        self.deleteButton = Button(self.buttonFrame, text="Delete", command=lambda reminder=self.reminder: Ribbon.removeReminder(reminder))
        
        self.labelFrame.pack(side="left", fill="both", expand=1)
        self.buttonFrame.pack(side="right", fill="both", expand=0)
        
        self.title.pack(side="top", fill="both", expand=1)
        self.message.pack(side="top", fill="both", expand=1)
        self.editButton.pack(side="top", fill="both", expand=1)
        self.deleteButton.pack(side="top", fill="both", expand=1)
        
        self.onModelChanged()
        
        
    def onModelChanged(self):
        self.title.configure(text=self.reminder.title)
        self.message.configure(text=self.reminder.message)
        