#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float32

rospy.init_node('ultrasonic')
pub = rospy.Publisher('distance',Float32, queue_size=1)
rate = rospy.Rate(20)

def reading(sensor):
    import time
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
     
    GPIO.setmode(GPIO.BOARD)
    TRIG = 11
    ECHO = 13
     
    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.03)
         
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
 
        while GPIO.input(ECHO) == 0:
          signaloff = time.time()
         
        while GPIO.input(ECHO) == 1:
          signalon = time.time()
 
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()
    else:
        print "Incorrect usonic() function varible."
         
i = 0

while i < 500:
        i += 1
        pub.publish(reading(0))
        rate.sleep()
