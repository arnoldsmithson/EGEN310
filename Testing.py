import PiMotor
import time
import RPi.GPIO as GPIO

#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#code is button type
#state is number
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
pwm = GPIO.PWM(3,50)
pwm.start(0)
#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)
#absolute axis event at 1572931328.122819, ABS_GAS
#event at 1572931344.985454, code 09, type 03, val 1023


#Button Assignment - if you change the controller, just use trial and error to find your own version of these numbers.
aBtn = 304
bBtn = 305
xBtn = 306
yBtn = 307
leftBump = 308
rightBump = 309
leftTrig = 10
rightTrig = 9
select = 310
start = 311
northSouthArrow = 17
eastWestArrow = 16

#start servo at default angle
kill = 0
angle = 7
pwm.ChangeDutyCycle(7)



#Goes over every button assignment and according function 
for event in gamepad.read_loop():
    print(event)
    if event.type == ecodes.EV_KEY or event.type == 3: # if button is pressed
        
        if event.value != 0:
            
            if event.code == aBtn: #user presses A button
                print("A Pressed")
                ab.on()
                motorAll.reverse(100)

                if angle != 7:
                    while angle < 7:
                        pwm.ChangeDutyCycle(angle + 1)
                        angle += 1
                        time.sleep(.1)
                    while angle > 7:
                        pwm.ChangeDutyCycle(angle -1)
                        angle -= 1
                        time.sleep(.1)
            elif event.code == bBtn: #user presses B button
                print("B Pressed")
                ar.on()
                m1.forward(38)
                m2.forward(38)
            elif event.code == yBtn: #user presses Y button
                print("Y Pressed")
                af.on()
                motorAll.forward(100)
               
            elif event.code == xBtn:#user presses X button
                print("X Pressed")
                al.on()
                m1.reverse(38)
                m2.reverse(38)
                
            elif event.code == leftBump: #user presses Left Bumper
                print("Left Bumper Pressed")
                GPIO.output(3,True)
                pwm.ChangeDutyCycle(angle-1)
                angle -= 1
                print(angle)
                GPIO.output(3,False)
            elif event.code == rightBump: #user presses Right Bumper
                print("Right Bumper Pressed ")
                GPIO.output(3,True)
                pwm.ChangeDutyCycle(angle + 1)
                angle += 1
                print(angle)
                GPIO.output(3,False)
            elif event.code == leftTrig: #user presses Left Trigger
                print("Left Trigger Pressed")
                ab.on()
                motorAll.forward(int((event.value/1023)*100))
            elif event.code == rightTrig: #user presses Right Trigger
                print("Right Trigger Pressed")
                af.on()
                motorAll.reverse(int((event.value/1023)*100))
                if angle != 7 and event.value >= int(1023/3):
                    while angle < 7:
                        pwm.ChangeDutyCycle(angle + 1)
                        angle += 1
                        time.sleep(.1)
                    while angle > 7:
                        pwm.ChangeDutyCycle(angle -1)
                        angle -= 1
                        time.sleep(.1)
            elif event.code == start:#user presses Start button
                m3.reverse(60)
                m4.reverse(60)
                ab.on()
                print("Start Button Pressed")
            elif event.code == select: #user presses Select Button
                print("Select Button Pressed")
            elif event.code == northSouthArrow: #user presses North or south DPad
                if event.value == 1:
                    m1.reverse(60)
                    m2.reverse(60)
                    ab.on()
                    print("Down Pressed")
                elif event.value == -1:
                    print("Up Pressed")
                else:
                    print("Direction Released")
            elif event.code == eastWestArrow: #user presses east or west DPad
                if event.value == 1:
                    print("Right Pressed")
                elif event.value == -1:
                    print("Left Pressed")
                else:
                    print("Direction Released")
        
        elif event.value == 0: #everything above but released
            if event.code == aBtn:
                print("A Released")
                ab.off()
                motorAll.stop()
            elif event.code == bBtn:
                print("B Released")
                ar.off()
                m1.stop()
                m2.stop()
            elif event.code == yBtn:
                print("Y Released")
                motorAll.stop()
                af.off()
            elif event.code == xBtn:
                print("X Released")
                al.off()
                m1.stop()
                m2.stop()
            elif event.code == leftBump:
                print("Left Bumper Released")
            elif event.code == rightBump:
                print("Right Bumper Released")
            elif event.code == leftTrig:
                motorAll.stop()
                ar.off()
                print("Left Trigger Released")
            elif event.code == rightTrig:
                motorAll.stop()
                af.off()
                print("Right Trigger Released")
            elif event.code == start:
                ar.off()
                m3.stop()
                m4.stop()
                print("Start Button Released")
            elif event.code == select:
                print("Select Button Released")
                kill += 1
                if(kill == 10):
                    break
            elif event.code == northSouthArrow or event.code == eastWestArrow:
                motorAll.stop()
                ar.off()
                al.off()
                af.off()
                ab.off()
                print("Direction Released")



pwm.stop()# stop servo and motors
GPIO.cleanup()
