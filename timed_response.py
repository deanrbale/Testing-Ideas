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
    
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False
        
    def run_response(self):
        response = ""
        while self._running and response == "":
             response = str(input("Enter your decision quickly: "))
        return response

    def run_timer(self, seconds, increment):
        second = seconds
        time.sleep(1)
        while self._running and second >= 0:
            if seconds == second:
                print()
            print("You have " + str(second) + " seconds left! " )
            print()
            if second == 0:
                break
                self._running = False
                self.terminate()
            time.sleep(increment)
            second -= increment

def quick_response():
    t_r = timed_response()
    # define skip_input_after_timout as a threading function, 5 as an argument
    quick_response_thread = threading.Thread(target=t_r.run_timer,args=(10,2,))
    quick_response_thread.setDaemon(True)
    # start threading
    quick_response_thread.start()
    # ask him his name
    R = str(t_r.run_response())
    if quick_response_thread.is_alive():
        #quick_response_thread._stop
        t_r.terminate()
        quick_response_thread.join()
        print("thank you")
    else:
        print("too late")
    input("")
    

quick_response()


   
   