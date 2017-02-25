'''
Primary model class. 
Model interaction from other modules should be performed through this class only.

Created on Feb 18, 2017

@author: Test
'''

from LinkedList import LinkedList
from Day import Day

class Calendar(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        super().__init__()
        self.calendar = {}
        
        
    def addReminder(self, reminder):
        
        year = reminder.when.year
        month = reminder.when.month
        day = reminder.when.day
        
        # insert new entries into the calendar if need be
        if year not in self.calendar:
            self.calendar[year] = dict()
            
        if month not in self.calendar[year]:
            self.calendar[year][month] = dict()
            
        if day not in self.calendar[year][month]:
            self.calendar[year][month][day] = Day()
            
        self.calendar[year][month][day].addReminder(reminder)
        
        
    def removeReminder(self, reminder):
        
        year = reminder.when.year
        month = reminder.when.month
        day = reminder.when.day
        
        if year in self.calendar and month in self.calendar[year] and day in self.calendar[year][month]:
            self.calendar[year][month][day].removeReminder(reminder)
            
            # now do cleanup
            
            if self.calendar[year][month][day].empty():
                del self.calendar[year][month][day]
                
                if len(self.calendar[year][month]) == 0:
                    del self.calendar[year][month]
                    
                    if len(self.calendar[year]) == 0:
                        del self.calendar[year]
        
        
    def getDay(self, year, month, day):
        return self.calendar[year][month][day] if year in self.calendar and month in self.calendar[year] and day in self.calendar[year][month] else LinkedList()
