Over the past 5 weeks we have been using a Joystick to control the speed and direction of the motors.  We have come to know that this is not always a viable option if one of us has the Joystick and the other doesn't.
Below is a list of methods and there names and ways to access them.




- Manual speed control via keyboard by @wallarug:

This method allows the user to specify the exact integer value between 0 - 255 and set the speed for the LEFT or RIGHT motor.
There is also an option to not send the data to a TCP server which would be handy if you were feeling a bit lazy.  Incorporated into Control module as of version Beta 1.3.
ACCESSIBLE VIA: debug\_value = "y"


- WASD via Keyboard by @wallarug:

This method uses the WASD keys on the keyboard to set the direction ONLY of the motors.  The only acceptable speeds at the moment are "on" and "off".  This method can NOT be used without TCP Server because TCP server is always on in this method. Incorporated into Control module as of version Beta 1.5.1 but not tested and stable until version Beta 1.5.3.
ACCESSIBLE VIA: debug\_value = "n"




- WASD Control with speed variation by @Ingramator:


Alpha stages - @Ingramator has not incorporated into Control module yet.






- Joystick Controller:


This has been incorporated into Control module since Alpha 0.1 and will remain the main control method.  There are three options:

> - pos

> - button

> - speed

> - all

The only one that should be used is pos, which has all the necessary commands to send to the TCP server (ACTIVE ALL THE TIME) and control the direction, speed and power going to the motors all the time.

"Button" is only used in Testing and tells us which button is being pressed on the Joystick.

"Speed" does not work in version up to and including Beta 1.5.3 but maybe fixed in a later version of the script.

"all" prints out the co-ordinates of the x-, y- and z-axis.  This was only used as a test and is still present but unused.




There maybe future changes to this page without notice.