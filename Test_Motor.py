#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

##This segment drives the motors in the direction listed below:
## forward and reverse takes speed in percentage(0-100)

try:
#-----------To Drive the Motors Forward------------# 
        print("Onward!")
        af.on()
        motorAll.forward(75)
        time.sleep(500)
#--------------------------------------------------#

#-----------To Drive the Motors backwards------------# 
        print("Retreat!")
        af.off()
        ab.on()
        motorAll.reverse(50)
        time.sleep(250)
#--------------------------------------------------#

#-----------To Drive the Motors Left---------------#
        print("Turn left!")
        ab.off()
        al.on()
        m1.stop()
        m2.stop()
        m3.forward(60)
        m4.forward(60)
        time.sleep(100)
#--------------------------------------------------#

#----------To Drive the Motors Right---------------#
        print("Turn Right!")
        ar.on()
        al.off()
        m1.forward(70)
        m2.forward(70)
        m3.stop()
        m4.stop()
        time.sleep(300)
#-------------------------------------------------#

#---------To Stop the Motors----------------------#
        print("Halt!")
        al.off()
        af.off()
        ar.off()
        motorAll.stop()
        time.sleep(275)
#-------------------------------------------------#

        
except KeyboardInterrupt:
    GPIO.cleanup()

    
