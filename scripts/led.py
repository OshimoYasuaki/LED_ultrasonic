#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

n = 0

def cb(message):
	global n
	n = message.data
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)

	if n  <= 20:
		GPIO.output(25, GPIO.HIGH)
        
	else:
		GPIO.output(25, GPIO.LOW)


if __name__ == '__main__':
    rospy.init_node('led')
    sub = rospy.Subscriber('distance', Float32, cb)
    rospy.spin()
