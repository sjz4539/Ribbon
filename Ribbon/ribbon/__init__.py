import pickle
from Monitor import Monitor
from Gui import Gui
from Calendar import Calendar
import Ribbon

from pathlib import Path
import datetime

if __name__ == '__main__':

    # unpickle queue from known file location
    if Path(Ribbon.save_location).is_file():
        file = open(Ribbon.save_location, 'rb')
        Ribbon.calendar = pickle.load(file)
    else:
        Ribbon.calendar = Calendar()
    
    # create GUI
    Ribbon.gui = Gui()
    
    # create monitor
    Ribbon.monitor = Monitor()
    
    # start monitor
    Ribbon.monitor.start()
    
    # init to today's date
    Ribbon.setSelectedDate(datetime.datetime.now().date())
    
    # start gui
    Ribbon.gui.mainloop()
    
    # stop monitor thread after gui exits
    Ribbon.monitor.stop()
    
    # basic operation:
    #   program loads any stored list of reminders and next group pointer on startup
    #   while running, program periodically (every second) checks the next reminder group in the queue, marked by an iterator or index
    #   while next reminder group trigger time < current time:
    #       while next reminder group has unfired reminders:
    #           fire next unfired reminder in group