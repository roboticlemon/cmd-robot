# Introduction #

Python does not come with all the required software to get you up and running.  Here is a page that tells you what you need to install to get up and running on each device involved in the set-up.


# Details #

**Windows Computers (Client)**

The Windows Operating System is used as the base station for this project due to the ease of access.  We use Python 2.7 throughout this project, therefore, we suggest using Python 2.7.  You will need to download and run the .exe file from this link: http://www.python.org/getit/ .  This file will install the IDLE program and the Python language for you.

Other software that is required AFTER you install Python 2.7 is:
  * pyserial (only used in testing)
  * pygame

This software can be found on downloads page and are also .exe files.


**Linux Boxes (Server)**

The Linux Operating System is used in this project as the receiver and wireless access point (as of 17/11/12).  Linux uses a service called "apt-get" to download and install all of its software.  The following command should install all the software that you require for the Linux Operating System (Raspberry Pi).

```
sudo apt-get install python-dev pyserial pygame
```

**Arduino IDE**

If editing the Arduino Sketch, you may need to install the Arduino IDE package on either the Windows or Linux operating System, depending on what takes your fancy (I suggest Windows, it is quicker).

For Linux:
```
sudo apt-get install arduino
```

For Windows:
  * Download the Arduino package located on the downloads page.