#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Mapulane Makhaba
Student Number:MKHMAP005
Prac: 1
Date: 25 June 2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

# Logic that you write
def main():
    #set output pin
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)

    while True:
	   #turning the Led ON
	   GPIO.output(7,True)
	   time.sleep(1)
	   #turing the Led OFF
	   GPIO.output(7,False)
	   time.sleep(1)

    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
