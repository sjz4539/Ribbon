'''
Created on Feb 18, 2017

@author: Steven Zuchowski
'''

import threading
import datetime
from tkinter import messagebox
import Ribbon

class Monitor(threading.Thread):
    
    def __init__(self):
        super().__init__()
        self.stop_flag = threading.Event()
        self.curDay = None
        self.setDay(datetime.datetime.now())
    
    
    def setDay(self, newDate=None):
        self.loadedDate = newDate if newDate is not None else datetime.datetime.now().date()
        self.curDay = Ribbon.calendar.getDay(newDate.year, newDate.month, newDate.day)
        
        curTime = datetime.datetime.now().time()
        
        while self.curDay.peek() is not None and self.curDay.peek().time <= curTime:
            self.curDay.getNext()
            
    
    def run(self):
        
        # until we're told to stop...
        while not self.stop_flag.wait(timeout=10):
            
            curDateTime = datetime.datetime.now()
            curTime = datetime.datetime.now().time()
            
            print("Monitor: Current time is " + str(curTime))
            print("Monitor: Next timeslot time is " + (str(self.curDay.peek().time) if self.curDay.peek() is not None else "None"))
            
            # if the next timeslots's trigger time has arrived or passed
            while self.curDay.peek() is not None and self.curDay.peek().time <= curTime:
                
                # fire the reminders in this timeslot
                for reminder in self.curDay.getNext():
                    messagebox.showinfo(reminder.title, reminder.message)
                    
            # check to make sure we're on the current day
            if self.loadedDate.day != curDateTime.day:
                self.setDay(curTime)
                    
        
    def stop(self):
        self.stop_flag.set()