# Introduction #

Throughout the construction of the robot we have developed and will continue developing a series of prototypes.

# Prototype 1 #

## General Info ##

Our first prototype was created on the 11th November which incorporated:

  * Ad-hoc network data exchange with network hosted on RPi (only after Monday the 12th November)
  * Control Module Beta version 1.5.6
  * 2 Motors powered by L293D H-Bridge IC

## Features ##

Prototype 1 featured:

  * Individual PWM control of 2 motors
  * Wireless network control
  * Joystick, WASD and debugging mode (alpha stage)

## Footage ##

Below is footage of prototype 1:

<a href='http://www.youtube.com/watch?feature=player_embedded&v=qzKx7UqiWZ4' target='_blank'><img src='http://img.youtube.com/vi/qzKx7UqiWZ4/0.jpg' width='425' height=344 /></a>

# Prototype 2 #

## General Info ##
Prototype 2 of CMDoverwatch incorporated mainly hardware changes. For the first time our robot was able to move around. This meant that the software we had written could be put to test in a real world situation.

## Features ##

Prototype 2 had the following features:

  * 2 **NEW** high speed motors
  * Ability to move around
  * Proper wheels and motor mounts onto a make-shift wooden frame
  * Wireless communication (cables required for power influx)

## Footage ##
<a href='http://www.youtube.com/watch?feature=player_embedded&v=m9JL0c9XgL4' target='_blank'><img src='http://img.youtube.com/vi/m9JL0c9XgL4/0.jpg' width='425' height=344 /></a>

## The death of Prototype two ##
<a href='http://www.youtube.com/watch?feature=player_embedded&v=BFQoKWN1UaM' target='_blank'><img src='http://img.youtube.com/vi/BFQoKWN1UaM/0.jpg' width='425' height=344 /></a>


# Alpha Build #

## General Info ##

CMDoverwatch Alpha was the first fully mobile unit which brought with it a series of other challenges.

## Features ##
  * 4 High powered, medium torque motors
  * Proper wooden ply chassis
  * Properly secured motor mounts
  * High powered antenna/router equiped
## Challenges ##
### Power ###
The first challenge was providing a sustainable solution to on board power. Early stages of the build used a series of AA batteries linked in series but due to their quick exhaustion by the 4 motors were replaced by 2 super heavy duty, rechargeable, 6V lantern batteries.

### Range ###
Being the first real experience we had with a roaming UGV wireless range became a problem. During several tests with the robot we found that the max range was about 70m. When the signal was lost the robot would continue with the last values and instruction set sent as there was no engine cut software upon detection of signal loss, end result, the robot hit a wall head on at full speed.

This setup was with only one high powered wireless adaptor on the UGV. To increase the range to over 150m (maximum testing distance in the test zone) we attached my Alfa UWS036H 1W high powered antenna to the client machine. The range and connection were exceptional and so we have stuck with this setup for the time being.

## Pictures ##

Pics of the alpha 2 build with upgraded wheels for speed, endurance and off road capabilty enhancements.

![http://imageshack.us/a/img705/2024/p1020624b.jpg](http://imageshack.us/a/img705/2024/p1020624b.jpg)
![http://imageshack.us/a/img716/2075/p1020625n.jpg](http://imageshack.us/a/img716/2075/p1020625n.jpg)
![http://imageshack.us/a/img841/2097/p1020626b.jpg](http://imageshack.us/a/img841/2097/p1020626b.jpg)
![http://imageshack.us/a/img208/5935/p1020627a.jpg](http://imageshack.us/a/img208/5935/p1020627a.jpg)

# Beta Build #

## General Info ##

Beta build is currently being worked on and consists of mainly cosmetic changes.

![http://imageshack.us/a/img248/6032/p1020671k.jpg](http://imageshack.us/a/img248/6032/p1020671k.jpg)
![http://imageshack.us/a/img19/4087/p1020670q.jpg](http://imageshack.us/a/img19/4087/p1020670q.jpg)
![http://imageshack.us/a/img820/8548/p1020669te.jpg](http://imageshack.us/a/img820/8548/p1020669te.jpg)


---


# CMDrecon #

# Alpha 1 #

## General Info ##

Work on CMDrecon has commenced and I am proud to announce that the first alpha build is complete! The build is 100% wired, currently feeding off computer power, not talking across a network and also completely unrefined for tank track use!

**IN PROGRESS**

## Features ##

  * Joystick, WASD and debug support
  * Wireless control
  * Self sufficient power supply
  * Rasberrypi controlled Arduino
  * Tom Board with L293D IC
  * PWM of both motors

## Needed to be done ##

  * Get a makeshift frame for mounting components
  * Refine and if necessary work on a new branch of the Control Module to include CMDrecon specific software enhancements like pivot turning and cruise control.
  * Attach webcam for remote viewing :)

Footage:

**Coming soon!**