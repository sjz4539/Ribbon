'''
Created on Feb 18, 2017

@author: Test
'''

from LinkedList import LinkedList

class ReminderQueue(LinkedList):
    '''
    classdocs
    '''
    
    def __init__(self):
        super().__init__()
        
    def addTimeSlot(self, timeslot):
        #find where this new timeslot belongs and insert it
        cur = self.head
        
        while not cur is None:
            # merge timeslots that match
            if cur.time == timeslot.time:
                cur.merge(timeslot)
                break
                
            # insert timeslots that don't have a match
            elif cur.time > timeslot.time:
                self.insert(timeslot, cur)
                break
            
            else:
                cur = cur.nextNode
            
        if cur is None:
            #failed to find a suitable spot, append the new timeslot
            self.append(timeslot)
        
    def removeTimeSlot(self, timeslot):
        self.remove(timeslot)