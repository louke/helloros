#!/usr/bin/env python
import rospy
import Adafruit_BBIO.GPIO as GPIO
import time

print "Encendiendo led..."
time.sleep(0.5)

GPIO.setup("P8_10", GPIO.OUT)
 
while True:
    GPIO.output("P8_10", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_10", GPIO.LOW)
    time.sleep(0.5)
