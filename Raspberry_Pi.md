# Introduction #

The Raspberry Pi is the Linux driven brain of both robots. It runs the TCP server and in the future will run other data servers. The Raspberry Pi is also in charge of status LEDs and other hardware such as amplifiers, speakers and wireless hardware. The Raspberry Pi is the device that will receive the wireless data and then write it through the serial port to the Arduino / ATMEGA.
# Specifications #

  * Device = Raspberry Pi Model B 512Mb RAM
  * Price = US$ 35
  * Operating system= many Linux flavours (Debian, Fedora) we are using a     Debian Wheezy fork named Rasbian (hard float)
  * Power = 3.5 W
  * CPU = ARM1176JZF-S (armv6k) 700 MHz, overclocked to 1 GHz
  * Storage capacity = SD card slot with 2/8GB card used (SDHC class 4/10)
  * Memory = 512 MB clocked at 500MHz
  * Graphics = Broadcom VideoCore IV

![http://www.raspberrypi.org/wp-content/uploads/2012/04/Raspi_Iso_Blue.png](http://www.raspberrypi.org/wp-content/uploads/2012/04/Raspi_Iso_Blue.png)

# Functions #

  * Handles wireless communication
  * Writes serial data to Arduino
  * On each robot there will be at least one Raspberry Pi that runs the TCP server (tcp.py)
  * Turns on/off/blinks status LEDs
  * Handles sound output
  * Handles LCD screen ouput

**Update!!** We will now be using Raspberry Pi Model A (see home page).  Raspberry Pi Model A has less power consumption and is therefore a better choice for this project.

![http://www.raspberrypi.org/wp-content/uploads/2012/09/sony-rasp-pi.jpg](http://www.raspberrypi.org/wp-content/uploads/2012/09/sony-rasp-pi.jpg)