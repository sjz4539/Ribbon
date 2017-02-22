'''
Created on Feb 19, 2017

@author: Test
'''
import unittest
from datetime import datetime
from Node import Node
from Reminder import Reminder
from Timeslot import Timeslot
from LinkedList import LinkedList
from ReminderQueue import ReminderQueue

class Test(unittest.TestCase):


    # Node Tests

    def testNodeConstructorA(self):
        node = Node()
        self.assertIsNone(node.nextNode, "nextNode should be None")
        self.assertIsNone(node.prevNode, "prevNode should be None")
        
        
    def testNodeConstructorB(self):
        a = Node()
        b = Node(a, None)
        self.assertIsNone(a.prevNode, "a.prevNode should be None")
        self.assertIsNone(a.nextNode, "a.nextNode should be None")
        self.assertIs(b.prevNode, a, "b.prevNode should be a")
        self.assertIsNone(b.nextNode, "b.nextNode should be None")
    
    
    def testNodeConstructorC(self):    
        a = Node()
        b = Node(None, a)
        self.assertIsNone(a.prevNode, "a.prevNode should be None")
        self.assertIsNone(a.nextNode, "a.nextNode should be None")
        self.assertIsNone(b.prevNode, "b.prevNode should be None")
        self.assertIs(b.nextNode, a, "b.nextNode should be a")
        
        
    def testNodeConstructorD(self):    
        a = Node()
        b = Node()
        c = Node(a, b)
        self.assertIs(c.prevNode, a, "c.prevNode should be a")
        self.assertIs(c.nextNode, b, "c.nextNode should be b")

    
    def testNodeInsertBehindA(self):
        a = Node()
        b = Node()
        
        a.insertBehind(b)
        
        self.assertIs(a.nextNode, b, "a.nextNode should be b")
        self.assertIs(b.prevNode, a, "b.prevNode should be a")


    def testNodeInsertBehindB(self):
        a = Node()
        b = Node()
        c = Node()
        
        a.insertBehind(b)
        b.insertBehind(c)
        
        self.assertIs(a.nextNode, b, "a.nextNode should be b")
        self.assertIs(b.prevNode, a, "b.prevNode should be a")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        
    
    def testNodeInsertBehindC(self):
        a = Node()
        b = Node()
        c = Node()
        
        a.insertBehind(b)
        a.insertBehind(c)
        
        self.assertIs(a.nextNode, c, "a.nextNode should be c")
        self.assertIs(c.prevNode, a, "c.prevNode should be a")
        self.assertIs(c.nextNode, b, "c.nextNode should be b")
        self.assertIs(b.prevNode, c, "b.prevNode should be c")  


    def testNodeInsertBeforeA(self):
        a = Node()
        b = Node()
        
        a.insertBefore(b)
        
        self.assertIs(a.prevNode, b, "a.prevNode should be b")
        self.assertIs(b.nextNode, a, "b.nextNode should be a")


    def testNodeInsertBeforeB(self):
        a = Node()
        b = Node()
        c = Node()
        
        a.insertBefore(b)
        b.insertBefore(c)
        
        self.assertIs(a.prevNode, b, "a.prevNode should be b")
        self.assertIs(b.nextNode, a, "b.nextNode should be a")
        self.assertIs(b.prevNode, c, "b.prevNode should be c")
        self.assertIs(c.nextNode, b, "c.nextNode should be b") 
        
        
    def testNodeInsertBeforeC(self):
        a = Node()
        b = Node()
        c = Node()
        
        a.insertBefore(b)
        a.insertBefore(c)
        
        self.assertIs(a.prevNode, c, "a.prevNode should be c")
        self.assertIs(c.nextNode, a, "c.nextNode should be a")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        
        
    def testNodeRemoveA(self):
        a = Node()
        b = Node()
        
        a.insertBehind(b)
        b.removeSelf()
        
        self.assertIsNone(a.nextNode, "a.nextNode should be none")
        
        
    def testNodeRemoveB(self):
        a = Node()
        b = Node()
        
        a.insertBehind(b)
        a.removeSelf()
        
        self.assertIsNone(b.prevNode, "b.prevNode should be none")
        
    
    def testNodeRemoveC(self):
        a = Node()
        b = Node()
        c = Node()
        
        a.insertBehind(b)
        b.insertBehind(c)
        b.removeSelf()
        
        self.assertIs(a.nextNode, c, "a.head should be c")
        self.assertIs(c.prevNode, a, "c.prevNode should be a")


    # LinkedList Tests
    
    def testLinkedListConstructor(self):
        a = LinkedList()
        self.assertIsNone(a.head, "a.head should be none")
        self.assertIsNone(a.tail, "a.tail should be none")
        self.assertIsNone(a.next, "a.next should be none")
        
    
    def testLinkedListAppendA(self):
        a = LinkedList()
        b = Node()
        
        a.append(b)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, b, "a.next should be b")
        
        
    def testLinkedListAppendB(self):
        a = LinkedList()
        b = Node()
        c = Node()
        
        a.append(b)
        a.append(c)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIsNone(b.prevNode, "b.prevNode should be none")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        self.assertIsNone(c.nextNode, "c.nextNode should be none")
        
    
    def testLinkedListAppendC(self):
        a = LinkedList()
        b = Node()
        c = Node()
        d = Node()
        
        a.append(b)
        a.append(c)
        a.append(d)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, d, "a.tail should be d")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIsNone(b.prevNode, "b.prevNode should be none")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        self.assertIs(c.nextNode, d, "c.nextNode should be d")
        self.assertIs(d.prevNode, c, "d.prevNode should be c")
        self.assertIsNone(d.nextNode, "d.nextNode should be none")
        
        
    def testLinkedListAppendD(self):
        a = LinkedList()
        b = Node()
        c = Node()
        d = Node()
        
        a.append(b)
        a.append(c)
        a.append(d, b)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIsNone(b.prevNode, "b.prevNode should be none")
        self.assertIs(b.nextNode, d, "b.nextNode should be d")
        self.assertIs(c.prevNode, d, "c.prevNode should be d")
        self.assertIsNone(c.nextNode, "c.nextNode should be none")
        self.assertIs(d.prevNode, b, "d.prevNode should be b")
        self.assertIs(d.nextNode, c, "d.nextNode should be c")
    
    
    def testLinkedListInsertA(self):
        a = LinkedList()
        b = Node()
        
        a.insert(b)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, b, "a.next should be b")
        
        
    def testLinkedListInsertB(self):
        a = LinkedList()
        b = Node()
        c = Node()
        
        a.insert(b)
        a.insert(c)
        
        self.assertIs(a.head, c, "a.head should be c")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, c, "a.next should be c")
        self.assertIsNone(c.prevNode, "c.prevNode should be none")
        self.assertIs(c.nextNode, b, "c.nextNode should be b")
        self.assertIs(b.prevNode, c, "b.prevNode should be c")
        self.assertIsNone(b.nextNode, "b.nextNode should be none")
        
    
    def testLinkedListInsertC(self):
        a = LinkedList()
        b = Node()
        c = Node()
        d = Node()
        
        a.insert(b)
        a.insert(c)
        a.insert(d)
        
        self.assertIs(a.head, d, "a.head should be d")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, d, "a.next should be d")
        self.assertIsNone(d.prevNode, "d.prevNode should be none")
        self.assertIs(d.nextNode, c, "d.nextNode should be c")
        self.assertIs(c.prevNode, d, "c.prevNode should be d")
        self.assertIs(c.nextNode, b, "c.nextNode should be b")
        self.assertIs(b.prevNode, c, "b.prevNode should be c")
        self.assertIsNone(b.nextNode, "b.nextNode should be none")
    
    
    def testLinkedListInsertD(self):
        a = LinkedList()
        b = Node()
        c = Node()
        d = Node()
        
        a.insert(b)
        a.insert(c)
        a.insert(d, b)
        
        self.assertIs(a.head, c, "a.head should be c")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, c, "a.next should be c")
        self.assertIs(d.prevNode, c, "d.prevNode should be c")
        self.assertIs(d.nextNode, b, "d.nextNode should be b")
        self.assertIsNone(c.prevNode, "c.prevNode should be none")
        self.assertIs(c.nextNode, d, "c.nextNode should be d")
        self.assertIs(b.prevNode, d, "b.prevNode should be d")
        self.assertIsNone(b.nextNode, "b.nextNode should be none")
            
    
    def testLinkedListRemoveA(self):
        a = LinkedList()
        b = Node()
        
        a.append(b)
        a.remove(b)
        
        self.assertIsNone(a.head, "a.head should be none")
        self.assertIsNone(a.tail, "a.tail should be none")
        self.assertIsNone(a.next, "a.next should be none")
        
    
    def testLinkedListRemoveB(self):
        a = LinkedList()
        b = Node()
        c = Node()
        
        a.append(b)
        a.append(c)
        a.remove(c)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIsNone(b.nextNode, "b.nextNode should be None")
        
        
    def testLinkedListRemoveC(self):
        a = LinkedList()
        b = Node()
        c = Node()
        
        a.append(b)
        a.append(c)
        a.remove(b)
        
        self.assertIs(a.head, c, "a.head should be c")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, c, "a.next should be c")
        self.assertIsNone(c.prevNode, "c.prevNode should be None")
        
        
    def testLinkedListRemoveD(self):
        a = LinkedList()
        b = Node()
        c = Node()
        d = Node()
        
        a.append(b)
        a.append(c)
        a.append(d)
        a.remove(c)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, d, "a.tail should be d")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIs(b.nextNode, d, "b.nextNode should be d")
        self.assertIs(d.prevNode, b, "d.prevNode should be b")
        
        
    def testLinkedListGetNext(self):
        a = LinkedList()
        b = Node()
        c = Node()
        a.append(b)
        a.append(c)
        
        self.assertIs(a.getNext(), b, "a.getNext() should return b first")
        self.assertIs(a.getNext(), c, "a.getNext() should return c second")
        self.assertIsNone(a.getNext(), "a.getNext() should return None last")
        

    # Reminder Tests
    
    def testReminderConstructorA(self):
        a = Reminder()
        self.assertEqual(a.title, "", "a.title should be blank")
        self.assertEqual(a.message, "", "a.message should be blank")
        self.assertFalse(a.triggered, "a.triggered should be false")
        
        
    def testReminderConstructorB(self):
        a = Reminder("title", None)
        self.assertEqual(a.title, "title", "a.title should be \"title\"")
        self.assertEqual(a.message, "", "a.message should be blank")
        
        
    def testReminderConstructorC(self):
        a = Reminder(None, "message")
        self.assertEqual(a.title, "", "a.title should be blank")
        self.assertEqual(a.message, "message", "a.message should be \"message\"")
        
        
    def testReminderSetTriggeredA(self):
        a = Reminder()
        self.assertFalse(a.triggered, "a.triggered should be false")
        
        a.setTriggered(True)
        self.assertTrue(a.triggered, "a.triggered should be true")

        
    # Timeslot Tests
    
    def testTimeslotConstructorA(self):
        a = Timeslot()
        self.assertIsNotNone(a.time, "a.time should not be None")
        
        
    def testTimeslotConstructorB(self):
        a = datetime.now() 
        b = Timeslot(a)
        self.assertIs(b.time, a, "b.time should be a")
        
        
    # ReminderQueue Tests
    
    def testAddTimeslotA(self):
        a = ReminderQueue()
        b = Timeslot(datetime(year=2017, month=2, day=1, hour=12))
        
        a.addTimeSlot(b)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, b, "a.tail should be b")
        self.assertIs(a.next, b, "a.next should be b")
    
        
    def testAddTimeslotB(self):
        a = ReminderQueue()
        b = Timeslot(datetime(year=2017, month=2, day=1, hour=12))
        c = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=10))
        
        a.addTimeSlot(b)
        a.addTimeSlot(c)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
    
    
    def testAddTimeslotC(self):
        a = ReminderQueue()
        b = Timeslot(datetime(year=2017, month=2, day=1, hour=12))
        c = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=10))
        
        a.addTimeSlot(c)
        self.assertIs(a.head, c, "a.head should be c")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, c, "a.next should be c")
        
        a.addTimeSlot(b)
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, c, "a.tail should be c")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        
        
    def testAddTimeslotD(self):
        a = ReminderQueue()
        b = Timeslot(datetime(year=2017, month=2, day=1, hour=12))
        c = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=10))
        d = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=20))
        
        a.addTimeSlot(b)
        a.addTimeSlot(c)
        a.addTimeSlot(d)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, d, "a.tail should be d")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        self.assertIs(c.nextNode, d, "c.nextNode should be d")
        self.assertIs(d.prevNode, c, "d.prevNode should be c")
        
        
    def testAddTimeslotE(self):
        a = ReminderQueue()
        b = Timeslot(datetime(year=2017, month=2, day=1, hour=12))
        c = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=10))
        d = Timeslot(datetime(year=2017, month=2, day=1, hour=12, minute=20))
        
        a.addTimeSlot(b)
        a.addTimeSlot(d)
        a.addTimeSlot(c)
        
        self.assertIs(a.head, b, "a.head should be b")
        self.assertIs(a.tail, d, "a.tail should be d")
        self.assertIs(a.next, b, "a.next should be b")
        self.assertIs(b.nextNode, c, "b.nextNode should be c")
        self.assertIs(c.prevNode, b, "c.prevNode should be b")
        self.assertIs(c.nextNode, d, "c.nextNode should be d")
        self.assertIs(d.prevNode, c, "d.prevNode should be c")
          

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()