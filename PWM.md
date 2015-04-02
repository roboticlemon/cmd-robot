# What is PWM? #

Pulse-width modulation (PWM)is a widely used technique for controlling power flow to electrical devices.

The average value of voltage (and inherently current) fed to the node is controlled by rapid switching the power source on and off. The proportion of on to off determines the amount of power the node will receive and is known as the duty cycle. The duty cycle can be encoded to send specific signals over a seemingly binary line with the help of a RTC however we are yet to implement such a function.


# Incorporation into CMDrobot #

In order to control the robot's motor speed the amount of voltage had to be varied. There were a couple of ways to tackle this, they are listed below:

  * **Option 1**

Our first option was to not have any speed control due to the difficulty  being too high. After evaluating the successive options we decided against this option as it would become a fundamental aspect of the project. Other elements of the design brief would be adversely affected (namely steering and RSS[slowing sequence](rapid.md))had we taken this route.

  * **Option 2**

The second option was to have a series of switchable transistors and/or relays creating individual paths with each path incurring a particular resistance or linking particular batteries into series to stipulate the various voltages. Using the Raspberry Pi GPIO interface we would be able to control the voltage flowing to the motors which would effectively give us speed control in large increments. The main draw backs with this option were cost, efficiency and instability. This system would cost hundreds to implement (high load bearing transistor and relay arrays) be inefficient and primitive in the way of speed control as well as introduce too many more variables (like the amount we had already wasn't enough)that could increase the probability of malfunction.

  * **Option 3**

Our third option was to investigate a method of voltage regulation called Pulse Width Modulation (PWM). The concept was easy to understand but would prove extremely difficult to implement. By varying the ratio of on to off switching we would be able to effectively and incredibly efficiently  control the speed of the motors from stall to maximum speed. With 256 possible values for output the option would fit nicely with the accuracy of the joystick.

After much discussion, research and consultation it was decided we would attempt to do this option and could fall back on option 2 if necessary.

# Problems with PWM #

The first real problem with PWM was the fact that the Raspberry Pi only had support for one channel. This meant we could only control the device going straight forwards or backwards (using a bit of relay switching and transistor work, normally it would only be able to go one direction) with both motors going at the same speed.

This problem had to be overcome- not on the RPi but off it. We investigated the Arduino developer boards and found that they were in line with our specifications- the next step was being able to bridge them. The simplest solution was to connect the Arduino to the RPi over serial and so initially we used serial over USB which would pass low level instructions to the microcontroller for physical output.