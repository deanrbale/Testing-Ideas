# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:11:02 2015

@author: Dean
"""
"""
http://chimera.labs.oreilly.com/books/1230000000393/ch12.html#_solution_197

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
...
c.terminate() # Signal termination
t.join()      # Wait for actual termination (if needed)
"""
###http://stackoverflow.com/questions/14029548/input-with-time-limit-countdown

import threading
import time

class timed_response():
    
    timed_out = False    
    
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, seconds, increment):
        timed_out = False
        second = seconds
        while self._running and second > 0:
            if seconds == second:
                print()
            print("You have " + str(second) + " seconds left: " )
            if second == 0:
                timed_out = True
                break
            time.sleep(increment)
            second -= increment
            

#    def skip_input_after_timout(seconds,increment):
#        """
#        Threading function, after N seconds print something and exit program
#        """
#        for second in range(seconds,-1,-increment):
#            time.sleep(increment)
#            if seconds == second:
#                print()
#                print("You have " + str(second) + " seconds left: " )
#                print("You did not enter a command quick enough!")
#                pass

def response():
    """
    Simple function where you ask him his name, if he answers
    you print message and exit
    """
    R = input("Enter you decision quickly!!!:")
    return R

def quick_response():
    t_r = timed_response()
    # define skip_input_after_timout as a threading function, 5 as an argument
    quick_response_thread = threading.Thread(target=t_r.run,args=(10,2,))
    quick_response_thread.setDaemon(True)
    # start threading
    quick_response_thread.start()
    # ask him his name
    N = None
    N = response()
    if N != None:
        #quick_response_thread._stop
        print("thank you")
    input(str(N) + " Now what: ")
    

quick_response()


   
   