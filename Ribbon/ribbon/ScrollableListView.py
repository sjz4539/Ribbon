'''
Created on Feb 20, 2017

@author: Steven Zuchowski
'''

from tkinter import Frame, Canvas, Scrollbar, Label

class ScrollableListView(Frame):
    
    def __init__(self, parent):
        
        self.items = list()
        
        super().__init__(parent)
        self.listCanvas = Canvas(self, borderwidth=2)
        self.listFrame = Frame(self.listCanvas)
        self.listScroller = Scrollbar(self, orient="vertical", command=self.listCanvas.yview)
        self.frameId = self.listCanvas.create_window(0, 0, window=self.listFrame, anchor="nw", tags="self.listFrame")
        self.listCanvas.configure(yscrollcommand=self.listScroller.set)
        
        self.listScroller.pack(side="right", fill="y")
        self.listCanvas.pack(side="left", fill="both", expand=1)
        
        self.listFrame.bind("<Configure>", self.onFrameConfigure)
        self.listCanvas.bind("<Configure>", self.onCanvasConfigure)
        
        self.listFrame.configure(width=self.listCanvas.winfo_width(), height=self.listCanvas.winfo_height())
        self.listFrame.columnconfigure(0, weight=1)
        

    def onFrameConfigure(self, event):
        self.listCanvas.configure(scrollregion=self.listCanvas.bbox("all"))
        
        
    def onCanvasConfigure(self, event):
        self.listCanvas.itemconfig(self.frameId, width=event.width)
        
        
    def addAll(self, items):
        for item in items:
            self.add(item)
        
        
    def add(self, item, pos=None):
        # if we don't already contain this item
        if not item in self.items:

            # insert it at the valid position given 
            # or append it to the end of our item list
            if pos is not None and len(self.items) >= pos:
                self.items.insert(pos, item)
                # update ourself to reflect the change
                self.onContentsChanged(pos)
            else:
                self.items.append(item)
                self.onContentsChanged(len(self.items) - 1)
            
    
    def remove(self, item):
        # if we contain the specified item
        if item in self.items:
            
            # mark its position in our list and remove it
            pos = self.items.index(item)
            self.items.remove(item)
            
            # tell the item to destroy the view it has for us
            item.destroyView(self.listFrame)
                
            # finally, update ourself to reflect the change
            self.onContentsChanged(pos)
            
    
    def removeAll(self):
        while len(self.items) > 0:
            self.remove(self.items[0])
            
            
    def onContentsChanged(self, start=0):
        # starting at the beginning of our item list or at the
        # specified valid position, update our contained widgets
        for i in range(start if start >= 0 and start < len(self.items) else 0, len(self.items)):
            # re-grid the view widget for this item so it inhabits the proper row
            self.items[i].getView(self.listFrame).grid(row=i, column=0, sticky=("N", "E", "S", "W"))
            
        self.onFrameConfigure(None)
        
            
    def onContentsDataChanged(self):
        for item in self.items:
            self.views[item].onModelChanged()
            
    