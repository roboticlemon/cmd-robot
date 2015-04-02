# Introduction #

This page is used to show the set-up of the motors when the motors failed.  Hopefully this will help debug and solve what would have caused the problem / fault.


# Details #

A few points before we continue:
  * There is four motors in this set-up
  * The motors are 19:1 Metal Gear-motors with 5 kg cm torque
  * We are using the Pololu Motor Shield (Dual-VNH5019-Motor-Shield)
  * Two motors are running out of each H-bridge
  * Running off 12 volts (2 x 6 volt lantern batteries)
  * PWM is used so that the motors are not always running off 12 volts and to vary the speed.
  * The Gertboard (and Raspberry Pi) are used as a substitute for the Arduino


## Some Diagrams ##

Below is the wiring diagram used to wire the Shield:

![http://www.gdriveurl.com/?idl=413648993491&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=413648993491&out=1&nonsense=something_that_ends_with.png)


Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages