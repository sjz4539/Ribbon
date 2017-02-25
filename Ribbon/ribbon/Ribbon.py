'''
Primary controller class. All cross-module calls should be directed here.

Created on Feb 18, 2017

@author: Steven Zuchowski
'''

# Ribbon
# A simple reminder app

# going to need:
#   Reminders - and event or notification to be displayed at some specified time
#   Reminder groups - groups of reminders that occur at the same time
#   Queue of reminder groups, sorted in ascending order by reminder time (first to occur = first in queue)
#   Means of storing/loading data on startup/shutdown (pickle)
#   GUI, including toast popups

save_location = "./ribbon.dat"

monitor = None
calendar = None
gui = None

selectedDate = None

def addReminder(reminder, refreshGui=True):
    calendar.addReminder(reminder)
    if reminder.when.date() == selectedDate:
        monitor.setDay(selectedDate)
        if refreshGui:
            showDate(selectedDate.year, selectedDate.month, selectedDate.day)


def editReminder(reminder):
    gui.showReminderDialog(reminder)


def removeReminder(reminder, refreshGui=True):
    calendar.removeReminder(reminder)
    if reminder.when.date() == selectedDate:
        monitor.setDay(selectedDate)
        if refreshGui:
            showDate(selectedDate.year, selectedDate.month, selectedDate.day)
    
    
def showDate(year, month, day):
    gui.showDate(year, month, day)
    
    
def getTimeslotsFor(year, month, day):
    return calendar.getTimeslotsFor(year, month, day)

    
def getDay(year, month, day):
    return calendar.getDay(year, month, day)


def setSelectedDate(newDate):
    globals()['selectedDate'] = newDate
    showDate(selectedDate.year, selectedDate.month, selectedDate.day)


def getSelectedDate():
    return selectedDate

