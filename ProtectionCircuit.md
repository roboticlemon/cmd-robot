# Introduction #

This page has a detailed list of the fuses that we use.  It has colour and Amperage and ... why not read on and see what you find.


# Details #

## Fuses ##

| **Amperage** | **Quantity Available** | **Have LED Status?** | **Colour** |
|:-------------|:-----------------------|:---------------------|:-----------|
| 5 | 12 | Yes | Orange |
| 7.5 | 8 | Yes | Brown |
| 15 | 2 | Yes | Blue |
| 20 | 2 | Yes | Yellow |
| 30 | 5 | Yes | Green |

**NOTE:** The above information is yet to be confirmed against stock.

**ALSO NOTE:** All the Fuses have the rated amperage engraved on the silver part of the Fuse (contact).

## Capacitors ##

We will use four capacitors (one on each motor) to soften the harsh effects of electric on the motor.  They will be 0.1 uF rated at 35 volts (ceramic - yet to be confirmed).

## Voltage Regulators ##

We will only be using a 5 volt @ 1.5A voltage regulator to power the Raspberry Pi and the Gertboard (ATMEGA 328p).  This is due to the USB powered hub not being able to power the robot (reliably) for more than 30 minutes.  Even if we used all of the powered USB banks, we could only get a reliable 90 minutes out of the robot.  This is not too bad but it would mean that between 25 - 40 minutes, a battery will die and knock-out the robot.

All other parts of the project do not use a voltage regulator at this point.