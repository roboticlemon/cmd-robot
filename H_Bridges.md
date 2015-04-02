# Introduction #

H-bridges allow for large current consuming devices, like motors, to be switched on an off (or have their speed varied). In our project we have 2 main H-bridge setups. The first setup is with the Polulu VNH5019 and the second is the L293D IC.


# Polulu VNH5019 #

The Pololu Dual VNH5019 Motor Driver Shield is built specifically for use with an Arduino. It is currently the H-bridge used for CMDoverwatch to operate the 4 motors.

## Features ##
The shield features:
  * Operating voltage range: 5.5 – 24 V1
  * High output current: up to 12 A continuous (30 maximum) per motor
  * Inputs compatible with both 5V and 3.3V systems
  * PWM operation up to 20 kHz, which is ultrasonic and allows for quieter motor operation
  * Motor indicator LEDs show what the outputs are doing even when no motor is connected
  * When used as a shield, the motor power supply can optionally be used to power the Arduino base as well
  * Can survive input voltages up to 41 V

## Pictures ##
http://a.pololu-files.com/picture/0J3753.600.jpg?bba16ba4b29c7648cb955b527c8d34c0
http://a.pololu-files.com/picture/0J3750.600.jpg?3185a4c89350cc2a51c19a7ed1f4dd2e
http://b.pololu-files.com/picture/0J3748.600.jpg?448e467f148f1ea5e4d6ba74a9a9bcab

# L293D IC #

The L293D IC is a quadruple half-H driver used in prototype 1,2 and CMDrecon. Future uses may include operating a PWM enabled robotic arm.

## Features ##

  * Wide Supply-Voltage Range: 4.5 V to 36 V
  * Separate Input-Logic Supply
  * Internal ESD Protection
  * Thermal Shutdown
  * High-Noise-Immunity Inputs
  * Output Current 600 mA Per Channel
  * Peak Output Current 1.2 A Per Channel
  * 16 Pin IC socket compatible
  * Inexpensive
  * Small and light
## NEW Schematic for CMDrecon, updated for pivot turning! ##

![http://img191.imageshack.us/img191/7136/newhbridgeschematic.png](http://img191.imageshack.us/img191/7136/newhbridgeschematic.png)


## Schematics ##

Below is an image of how the L293D was used in CMDoverwatch prototypes but also in the current CMDrecon builds. It allows for bidirectional control of 2 motors (or 4 if linked in parallel).

![http://img404.imageshack.us/img404/9972/hbridgeschematic.png](http://img404.imageshack.us/img404/9972/hbridgeschematic.png)