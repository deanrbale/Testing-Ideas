# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:11:02 2015

@author: Dean
"""

###http://stackoverflow.com/questions/14029548/input-with-time-limit-countdown

import threading
import time
import os

def timed_response():
    """
    Simple function where you ask him his name, if he answers
    you print message and exit
    """
    response = input("Enter you decision quickly!!!:")
    return response

def exit(msg):
    """
    Exit function, prints something and then exits using OS
    Please note you cannot use sys.exit when threading..
    You need to use os._exit instead
    """
    print(msg)
    
    #os._exit(1)

def skip_input_after_timout(seconds,increment):
    """
    Threading function, after N seconds print something and exit program
    """
    for second in range(seconds,-1,-increment):
        time.sleep(increment)
        if seconds == second:
            print()
        print("You have " + str(second) + " seconds left: " )
    print("You did not enter a command quick enough!")
    pass

def quick_response():
    # define skip_input_after_timout as a threading function, 5 as an argument
    quick_response_thread = threading.Thread(target=skip_input_after_timout,args=(10,2,))
    quick_response_thread.setDaemon(True)
    # start threading
    quick_response_thread.start()
    # ask him his name
    N = None
    N = timed_response()
    if N != None:
        #quick_response_thread._stop
        print("thank you")
    input(str(N) + " Now what: ")
    

quick_response()


   
   