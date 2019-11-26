# EGEN310

Final commented code in a github (or similar) repository with a user readme file and a developer readme file.  Clearly indicate which code was written by your CS designer.

This code was largely grabbed from a provided github repository bought with the acquisition of a Raspberry Pi MotorShield from Amazon.

The file coded completely by the CS team member is Testing.py. Test_Motor.py was used to make sure the motors were functional when wired properly into the Motor Shield.

For Usage: In order for Testing.py to work on the raspberry pi, the pi must be booted headless with no bluetooth or USB input devices attached so the controller will take the first input device spot guaranteed. This makes for no room for error upon starting the program and maintaining operation of the vehicle.

For modification: The user must change the input device folder variable on line 10 to their specified input device. Once that happens, they'll need to run a specific program via the command prompt in the OS to grab the numbers of every input button on the device, and make variables accordingly. The logic in the if statements can be amended for specific corresponding variables. Any action the button needs to do can be modified in the if statements as well.

Approximate hours needed for completion of program: 10-15 hours, including research, testing, implementation, and debugging.
