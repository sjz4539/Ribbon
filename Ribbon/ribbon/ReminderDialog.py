'''
Created on Feb 23, 2017

@author: Test
'''
from tkinter import Toplevel, Label, Entry, Button
import Ribbon
from Reminder import Reminder
from DateChooser import DateChooser
from TimeChooser import TimeChooser
from datetime import datetime

class ReminderDialog(Toplevel):
    '''
    classdocs
    '''

    def __init__(self, parent, reminder=None, initialDate=None):
        super().__init__(parent)
        
        self.reminder = reminder
        initialDate = datetime.now().date() if self.reminder is None else self.reminder.when.date()
        initialTime = datetime.now().time() if self.reminder is None else self.reminder.when.time()
        
        
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.title("New Reminder..." if reminder is None else "Edit Reminder...")
        self.geometry("+%d+%d" % (parent.winfo_rootx()+25, parent.winfo_rooty()+25))
        
        Label(self, text="Title:").grid(row=0, column=0, sticky=("W"))
        self.title = Entry(self)
        self.title.delete(0, "end")
        self.title.insert(0, "Reminder Title" if self.reminder is None else self.reminder.title)
        self.title.grid(row=0, column=1)
        
        Label(self, text="Message:").grid(row=1, column=0, sticky=("W"))
        self.message = Entry(self)
        self.message.delete(0, "end")
        self.message.insert(0, "Something happened!" if self.reminder is None else self.reminder.message)
        self.message.grid(row=1, column=1)
        
        Label(self, text="Date:").grid(row=2, column=0, sticky=("W"))
        self.date = DateChooser(self, initialDate)
        self.date.grid(row=2, column=1)
        
        Label(self, text="Time:").grid(row=3, column=0, sticky=("W"))
        self.time = TimeChooser(self, initialTime)
        self.time.grid(row=3, column=1)
        
        Button(self, text="OK", command=self.ok).grid(row=4, column=0)
        Button(self, text="Cancel", command=self.cancel).grid(row=4, column=1)
        
    
    def ok(self, event=None):
        date = self.date.getSelectedDate()
        time = self.time.getTime()
        
        if self.reminder is None:
            Ribbon.addReminder(Reminder(datetime(year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute), self.title.get(), self.message.get()))
        else:
            # when editing, need to remove this reminder and re-add it to the proper location.
            Ribbon.removeReminder(self.reminder)
            self.reminder.title = self.title.get()
            self.reminder.message = self.message.get()
            self.reminder.when = datetime(year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute)
            Ribbon.addReminder(self.reminder)
            
        self.cancel(event)
     
    
    def cancel(self, event=None):
        self.parent.focus_set()
        self.destroy()   
        