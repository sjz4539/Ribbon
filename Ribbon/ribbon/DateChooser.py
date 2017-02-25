'''
Created on Feb 20, 2017

@author: Test
'''

from tkinter import Frame, Button, Label
from tkinter.font import Font
from datetime import date
from calendar import monthrange, month_name

class DateChooser(Frame):
    '''
    classdocs
    '''

    def __init__(self, parent, initialDate=None):
        
        super().__init__(parent)
        self.callback = None
        self.normalFont = Font(self, size="9", weight="normal")
        self.boldFont = Font(self, size="9", weight="bold")
        
        if initialDate is None:
            initialDate = date.today()
        
        # initialize month+year to current
        d = initialDate
        self.displayedYear = d.year
        self.displayedMonth = d.month
        
        # track selected item
        self.selectedYear = d.year
        self.selectedMonth = d.month
        self.selectedDay = d.day
        self.selectedIndex = None
        
        # top button bar components: create, assemble, bind
        self.prevButton = Button(self)
        self.nextButton = Button(self)
        self.topLabel = Label(self)
            
        self.prevButton.grid(row=0, column=0)
        self.topLabel.grid(row=0, column=1, columnspan=5)
        self.nextButton.grid(row=0, column=6)
        
        self.prevButton.bind("<Button-1>", self.prevMonth)
        self.nextButton.bind("<Button-1>", self.nextMonth)
        
        
        # DoW header components: create, assemble
        Label(self, text="S").grid(row=1, column=0)
        Label(self, text="M").grid(row=1, column=1)
        Label(self, text="T").grid(row=1, column=2)
        Label(self, text="W").grid(row=1, column=3)
        Label(self, text="R").grid(row=1, column=4)
        Label(self, text="F").grid(row=1, column=5)
        Label(self, text="Z").grid(row=1, column=6)
        
        
        # calendar page components
        self.selectorFrame = Frame(self)
        self.dateLabels = []
        
        for i in range(0, 42):
            self.dateLabels.append(Label(self.selectorFrame, font=self.normalFont))
            self.dateLabels[i].grid(row=i//7, column=i%7)
            self.dateLabels[i].bind("<Button-1>", lambda event, index=i: self.onDateClicked(index))
            
        self.selectorFrame.grid(row=2, rowspan=5, columnspan=7)
        
        # initialize calendar page to the current month    
        self.updateDateLabels()
        
    
    def updateDateLabels(self):
        
        d = date(self.displayedYear, self.displayedMonth, 1)
        m = monthrange(self.displayedYear, self.displayedMonth)[1]
        w = (d.weekday()+1)%7 # deal with weekday() being monday to sunday (0-6) by converting to sunday-saturday
        
        # update top label to reflect displayed month+year
        self.topLabel.configure(text=str(month_name[self.displayedMonth] + " " + str(self.displayedYear)))
        
        # blank day labels before first of the displayed month
        for i in range(0, w):
            self.dateLabels[i].configure(text="")
            self.dateLabels[i].day = None
        
        # set text on labels for days of the displayed month    
        for i in range(0, m):
            self.dateLabels[w + i].configure(text=str(i+1))
            self.dateLabels[w + i].day = i+1
            if i+1 == self.selectedDay and self.selectedIndex is None:
                self.selectedIndex = w+i
        
        # blank day labels after the last day of the displayed month    
        for i in range(w + m, len(self.dateLabels)):
            self.dateLabels[i].configure(text="")
            self.dateLabels[i].day = None
        
        # update color of selected item depending on visibility
        if self.selectedIndex is not None:
            if self.displayedYear == self.selectedYear and self.displayedMonth == self.selectedMonth:
                self.dateLabels[self.selectedIndex].configure(fg="blue", font=self.boldFont)
            else:
                self.dateLabels[self.selectedIndex].configure(fg="black", font=self.normalFont)
            
    
    def onDateClicked(self, index):
        if self.dateLabels[index].day is not None:
            
            # reset previous selection color
            if self.selectedIndex is not None:
                self.dateLabels[self.selectedIndex].configure(fg="black", font=self.normalFont)
            
            # update new selection
            self.selectedYear = self.displayedYear
            self.selectedMonth = self.displayedMonth
            self.selectedDay = self.dateLabels[index].day
            self.selectedIndex = index
            self.dateLabels[self.selectedIndex].configure(fg="blue", font=self.boldFont)
            
            # call any set callback
            if self.callback is not None:
                self.callback(self.getSelectedDate())
            

    def setOnDateSelected(self, callback):
        # callback must accept three arguments:
        #    selected year, selected month, selected day
        self.callback = callback
            
    
    def getSelectedDate(self):
        return date(year=self.selectedYear, month=self.selectedMonth, day=self.selectedDay)
    
    
    def prevMonth(self, event):
        if self.displayedMonth == 1:
            self.displayedYear -= 1
            self.displayedMonth = 12
        else:
            self.displayedMonth -=1
    
        self.updateDateLabels()
    
    
    def nextMonth(self, event):
        if self.displayedMonth == 12:
            self.displayedYear += 1
            self.displayedMonth = 1
        else:
            self.displayedMonth += 1
    
        self.updateDateLabels()
    
    
    