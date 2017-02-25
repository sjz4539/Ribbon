'''
Created on Feb 20, 2017

@author: Steven Zuchowski
'''

from ScrollableListView import ScrollableListView
import Ribbon

class DayView(ScrollableListView):
    
    def __init__(self, parent):
        super().__init__(parent)
        
    
    def showDate(self, year, month, day):
        # clear our displayed items
        self.removeAll()

        # add the view for each reminder for the selected day
        for reminder in Ribbon.getDay(year, month, day):
            self.add(reminder)


    def onReminderChanged(self, reminder):
        pass