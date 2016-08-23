#!/usr/bin/env python

import ZeroSeg.led as led
import RPi.GPIO as GPIO
import time
#from datetime import datetime
import datetime

# init

#1 = left
switch1 = 17
switch2 = 26

GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)

device = led.sevensegment(cascaded=2)

def ceil_dt(dt=None, delta=60):
    return dt + (datetime.datetime.min - dt) % delta 

def ceil_dt(dt, delta=60):
    return dt + datetime.timedelta(minutes = delta - dt.minute % delta,
                                       seconds = -(dt.second % 60),
					microseconds = -(dt.microsecond % 1000000))

# Display hh.mm for datetime object
def displaytime(device, deviceId, dt):
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    dot = second % 2 == 0                # calculate blinking dot
    # Set hours
    device.letter(deviceId, 4, int(hour / 10))     # Tens
    device.letter(deviceId, 3, hour % 10, dot)     # Ones
    # Set minutes
    device.letter(deviceId, 2, int(minute / 10))   # Tens
    device.letter(deviceId, 1, minute % 10)        # Ones

# Indicate parking with letter P
def displaypark(device, deviceId):
    device.letter(deviceId, 8, 'p')

# Indicate something is happening to the user
def displayaction(device, deviceId):
    for x in xrange(1,9,1):
        device.letter(deviceId, x, '-')
    time.sleep(0.3)
    device.clear(deviceId)
    time.sleep(0.3)
    for x in xrange(1,9,1):
        device.letter(deviceId, x, '-')
        device.letter(deviceId, x, '-')
    time.sleep(0.4)
    device.clear(deviceId)

level = 1
parked = None
counter = 0

while True:
    counter += 1
    if not GPIO.input(switch1):
        if parked == None:
        	parked = datetime.datetime.now()
        else:
        	parked = None
        print "Button 1 pressed, set parking time to: %s" % parked
	displayaction(device, 1)
     
    elif not GPIO.input(switch2):
	level = 1 + ( level % 15 )
        device.brightness(level)
        print "Button 2 pressed, increased brightness to: %s" % level
	displayaction(device, 1)

    # only update display every 1 seconds
    if counter % 100 == 0:
        if parked == None:
            displaytime(device, 1, dt = datetime.datetime.now())
        else:
            displaypark(device, 1)
    	    # parking time rounded to nearest following 30min
            displaytime(device, 1, dt = ceil_dt(parked, 30))
    # sleep 1/100 sec
    time.sleep(1.0/100)

