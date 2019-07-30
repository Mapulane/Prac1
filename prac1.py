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

#count up function
def up(channel):
	global count
	if count >=7:
		count=0
	else:
		count+=1
	display(count)
#count down function
def down(channel):
	global count
	if count <= 0:
		count=7
	else:
		count-=1
	display(count)
#write output to LEDS
def display(count):
	binary=bin(count) #convert num into binary
	binlist=binary[2:]
	binlist = list(map(int, binlist)) #store the binary value into a list

	while len(binlist) <3:
		binlist.insert(0,0)
	#write output to the LEDS
	chan_list = (36,38,40)
	GPIO.output(chan_list, (binlist[0],binlist[1],binlist[2]))

#initalise  board mode
count = 0
GPIO.setmode(GPIO.BOARD)

#set output pin
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

#set input pin
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#set up interrupts
GPIO.add_event_detect(31,GPIO.FALLING, callback = up, bouncetime=400)
GPIO.add_event_detect(32,GPIO.FALLING, callback = down, bouncetime=400)

# Logic that you write
def main():
	pass
	
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
GPIO.cleanup()
