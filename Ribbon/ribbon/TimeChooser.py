'''
Created on Feb 23, 2017

@author: Test
'''
from tkinter import Frame, Spinbox, Label
from datetime import datetime, time

class TimeChooser(Frame):
    '''
    classdocs
    '''

    def __init__(self, parent, initialTime=None):
        super().__init__(parent)
        
        if initialTime is None:
            initialTime = datetime.now().time()
        
        self.hour = Spinbox(self, from_=1, to=12, width=3)
        self.hour.grid(column=0, row=0)
        Label(self, text=":").grid(column=1, row=0)
        self.minute = Spinbox(self, from_=00, to=59, format="%02.0f", width=3)
        self.minute.grid(column=2, row=0)
        self.ampm = Spinbox(self, values=("AM", "PM"), width=4)
        self.ampm.grid(column=3, row=0)

        # set AM/PM
        self.ampm.delete(0, "end")
        self.ampm.insert(0, "AM" if initialTime.hour < 12 else "PM")
        
        # set hour, 12-hour display
        self.hour.delete(0, "end")
        if initialTime.hour == 0:
            self.hour.insert(0, "12")
        elif initialTime.hour <= 12:
            self.hour.insert(0, str(initialTime.hour))
        else:
            self.hour.insert(0, str(initialTime.hour - 12))
            
        # set minute    
        self.minute.delete(0, "end")
        self.minute.insert(0, "{:0>2d}".format(initialTime.minute))
        
        # readonly the entry widgets
        self.hour.config(state="readonly")
        self.minute.config(state="readonly")
        self.ampm.config(state="readonly")
        
 
    def getTime(self):
        hour = int(self.hour.get())
        if self.ampm.get() == "AM":
            hour %= 12
        elif hour < 12:
            hour += 12 
            
        return time(hour=int(hour), minute=int(self.minute.get()))

        
        