# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:11:02 2015

@author: Dean
"""
"""
http://chimera.labs.oreilly.com/books/1230000000393/ch12.html#_solution_197
http://stackoverflow.com/questions/14029548/input-with-time-limit-countdown
"""
#import relevent packages
import threading
import time

class timed_response():     
    
    valid_input = True   
    
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False
        
    def run_response(self):
        #While the thread is running accept a response is not yet been given ask for one
        response = ""
        while self._running and response == "":
             response = str(input("Enter your decision quickly: "))
        return response

    def run_timer(self, seconds, increment):
        second = seconds
        #Pause to allow for the run_response to start
        time.sleep(1)
        #While the thread is running and the counter has not reached zero
        while self._running and second >= 0:
            if seconds == second:
                print()
            #Display time left
            print("You have " + str(second) + " seconds left! " )
            print()
            #Check whether time has ran out
            if second == 0:
                #Give an appropiate command
                print("You were too slow, press ENTER to see what happens to you now.")
                self.valid_input = False
                #Terminate thread
                self.terminate()
            #Pause for increment amount of time
            time.sleep(increment)
            #Reduce time left
            second -= increment

def quick_response(max_time,increment):
    timed_response_class = timed_response()
    # define timed_response_class.run_timer as a threading function
    quick_response_thread = threading.Thread(target=timed_response_class.run_timer,args=(max_time,increment,))
    #set the thread to daemon mode
    quick_response_thread.setDaemon(True)
    # start threading
    quick_response_thread.start()
    # ask user for action (may need to take loop from function and place here when validation checks are present)
    action = str(timed_response_class.run_response())
    #If the thread is still running, the user has entered a valid action (need valid check here)
    if quick_response_thread.is_alive():
        #terminate the thread
        timed_response_class.terminate()
        #wait for actual termination
        quick_response_thread.join()
    #check to see if there was a valid input with the time
    if not timed_response_class.valid_input:
        action = ""
    return action
    
#test
response = ""
response = quick_response(15,3)
if response != "":
    print("thank you")
else:
    print("oh no")

   
   