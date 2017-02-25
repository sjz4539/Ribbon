'''
Created on Feb 22, 2017

@author: Test
'''
from LinkedList import LinkedList
from Timeslot import Timeslot

class Day(LinkedList):
    '''
    classdocs
    '''

    def __init__(self):
        super().__init__()
        
        
    def addReminder(self, reminder):
        self.getTimeslot(reminder.when.time()).append(reminder)
        
        
    def removeReminder(self, reminder):
        for slot in self:
            if reminder in slot:
                slot.remove(reminder)
                if slot.empty():
                    self.remove(slot)
                break
                         

    def getTimeslot(self, time):
        # scan all timeslots
        for slot in self:
            # found a match, return it
            if slot.time == time:
                return slot
            
            #found a slot after the time we want, insert in front of it
            elif slot.time > time:
                newSlot = Timeslot(time)
                self.insert(newSlot, slot)
                return newSlot
              
        # time is after all timeslots in this day, append
        newSlot = Timeslot(time)
        self.append(newSlot)
        
        return newSlot
    
    