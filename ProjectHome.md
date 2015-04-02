![http://img203.imageshack.us/img203/5191/cmdrobotnew.png](http://img203.imageshack.us/img203/5191/cmdrobotnew.png)



# The Project #

The CMDrobot project incorporates all mechatronic engineering disciplines; mechanical, electronic, computer, software, control and systems design. The project founders are **Tom Ingram** and **Cian Byrne**. The  aim of the CMDrobot project is to create a network of robots which can wirelessly communicate with base stations as well as mobile field agents. The robots are able to move about to provide real time and lapsed data back to CMDhq for use by various software clients. Information capable of being received includes video/audio feeds, GPS coordinates, nearby network information, detected hazards and on board component statuses.


![http://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Mecha_workaround.svg/240px-Mecha_workaround.svg.png](http://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Mecha_workaround.svg/240px-Mecha_workaround.svg.png)

The project involves the construction of two "CMDrobots". The larger of the two is named "CMDoverwatch" the smaller being named "CMDrecon".

## OPSEC CLASSIFIED- Missiles currently beta testing ##

## Programming Languages ##

Throughout the course of the project we have experimented and used a variety of programming languages including:
  * Python
  * Visual Basic
  * C++
  * Bash

Every language has a part in the project which is detailed below!

### C# ###

NEW Language used primarily in Windows Phone app development. For desktop/laptop/tablet software we will be sticking to VB.NET for now. More info to come.

### Visual Basic (.NET) ###
![http://www.tabsstudio.com/vs_logo.png](http://www.tabsstudio.com/vs_logo.png)

The entire client side of the project is now entirely written in Visual Basic (VB). Originally done in Python, we decided to move so that we could:
  * Work in an object oriented environment (GUI)
  * Seamlessly port code across Windows 8, RT and Phone 8
  * Not rely on external modules and dependencies
  * Have all code in one place
  * Use the deep level collaboration tools in Visual Studio 2012
  * Dig into the rich .NET APIs
  * Take advantage of new hardware

Visual Basic handles:
  * Joystick detection and input
  * Raw conversion and decoding algorithms
  * Robot movement and stimuli logic
  * TCP communication over WiFi
  * Video and audio feed using M-JPEG

### Python ###
<img src='http://www.python-course.eu/images/python-logo.png' alt='Smiley face' width='300' height='100'>

The main programming language used throughout the project was Python 2.7. Python has since been made redundant on the client side, with the porting of code to VB, however it still plays a vital role server side. On the server, Python handles:<br>
<br>
<ul><li>Raspberry Pi based Logic and processing<br>
</li><li>TCP communication back to command and control<br>
</li><li>GPIO input/output (screens, status/signal LEDs and switches)<br>
</li><li>On board lighting<br>
</li><li>Intelligent munition systems</li></ul>



<h3>C++</h3>
Another language used in the project is C++ which is used in programming the Arduino and GertBoard ATMega microprocessor. C++ handles:<br>
<br>
<ul><li>Motor speed and direction control<br>
</li><li>Status LED states, switch postions and numerous sensor inputs</li></ul>

<a href='http://www.generationrobots.de/site/medias/Arduino-Logo.JPG'>http://www.generationrobots.de/site/medias/Arduino-Logo.JPG</a>

<h3>Bash</h3>

Bash is a scripting language used in Linux to do basic scripting. We use bash to launch Python scripts as well as install custom custom software, run diagnostics on the hardware and automate troubleshoot tasks.<br>
<br>
<img src='http://b.dryicons.com/images/icon_sets/coquette_part_5_icons_set/png/128x128/windows_terminal.png' />

<h2>CMDoverwatch</h2>

<a href='https://code.google.com/p/cmd-robot/wiki/Prototypes#Alpha_Build'>CMDoverwatch</a> is the larger of the two Unmanned Grounds Vehicles (UGVs). It has four wheel drive capabilities and so designed for all terrain. Capable of speeds close to 100km/h with extreme turbo mode the UGV is able to quickly evade hostile situations. Steering is speed based meaning that one side of the craft is slowed to allow for turning. The main purposes of this robot:<br>
<br>
<ul><li>Act as a base station relaying wireless signals from CMDcontrol to other satellites<br>
</li><li>Carry large weights<br>
</li><li>Provide direct infiltration for CMDrecon with its drive in drive out loading ramp<br>
</li><li>Provide over watch with rotatable camera, ultrasonic beamer, infrared lighting and microphone</li></ul>

<h4>Features</h4>
<ul><li>Four high powered, high torque motors running off 12/24 VDC with 500RPM@12VDC<br>
</li><li>4WD, (no option for 2WD selection because of gearbox limitations)<br>
</li><li>Voltage selection mode at 12V, 24V, 33V and ~60V intervals<br>
</li><li>Turbo modes at 33V and ~60V to allow maximum speed of 100km/h<br>
</li><li>Fully wireless transmission over 802.11g WiFi using TCP<br>
</li><li>Wireless IP camera<br>
</li><li>LCD screen for printing valuable data such as IP address (discontinued, debugging purposes only)<br>
</li><li>Autopilot mode for use when reliable connection cannot be achieved, robot will make its way to last known established connection point<br>
</li><li>Power saving mode with asset shutdown and power transfer from emergency bank to vital banks<br>
</li><li>Self destruct capability with secure SD card wipe</li></ul>

<h2>CMDrecon</h2>

CMDrecon is the smaller of the two UGVs. It has two (possibly four in the future) medium powered motors driving tank tracks. This device is primarily used for recon once deployed from CMDoverwatch. Being lightweight and highly mobile this device can be transported by other satellite robots for infiltration into a militarised zone.<br>
<br>
<h4>Features</h4>

<ul><li>2 rubber tank tracks for off-road use<br>
</li><li>6 AA batteries and one 2600 mAh battery for on board embedded systems<br>
</li><li>2 medium power motors running @6VDC<br>
</li><li>Low power consumption at cruising speed<br>
</li><li>Turbo mode for ability to double max speed<br>
</li><li>Wireless IP camera with pan, tilt and digital zoom capabilities<br>
</li><li>Automatic night vision mode with Infrared LEDs to illuminate 3m+ in front of vehicle</li></ul>

<b>Notice</b> Construction has begun as of 10/12/12!<br>
<br>
Offical Youtube Page: <a href='https://www.youtube.com/user/CMDenterprises'>https://www.youtube.com/user/CMDenterprises</a>

Un-Offical Youtube page: <a href='http://www.youtube.com/user/wallarug?feature=mhee'>http://www.youtube.com/user/wallarug?feature=mhee</a>

<h1>Things that need to be done:</h1>

<h3>CMDoverwatch</h3>
<ul><li><del>Increase speed! Almost done!</del> <b>COMPLETE</b>
</li><li><del>More effective weight distribution</del> <b>COMPLETE</b>
</li><li><del>Enhance software to improve driving <b>CRITICAL</b></del> <b>COMPLETE</b>
</li><li>Attach wireless camera and setup streaming (complete need to integrate streaming into software) <b>progress being made with new Raspberry Pi Camera Module</b>
</li><li><del>Variable WASD control /Up,Right,Left,Down # BETA</del> <b>Depreciated</b>
</li><li>Make schematics for turbo mode (Ingram will revisit :D )<br>
</li><li>Complete a PCB design<br>
</li><li><del>Make the wheels more accurate and stable</del> <b>COMPLETE</b>
<h3>CMDrecon</h3>
</li><li><del>Modify code for enhancement with robot tracks (works fine but optimisation for pivot turning needed)</del> <b>COMPLETE</b>
</li><li><del>Package all components into a secure box that's screwed on</del> <b>COMPLETE</b>
<h3>Project page</h3>
</li><li>Better Wiki page coverage<br>
</li><li>Date what we have been doing<br>
</li><li>Create more issues on issues page for tracking progress.<br>
</li><li>Add more pictures of all robots<br>
</li><li><del>Move all images to a Skydrive account (or Google) <b>URGENT</b></del> <b>COMPLETE</b></li></ul>

<h2>UPDATES!!</h2>

<h3>Raspberry Pi Hardware Guide</h3>
The Raspberry Pi Hardware Guide is now on the Google Play store.  This app has been designed to help Raspberry Pi Users with basic and complicated set up of the Raspberry Pi.  Take a look at it on the play store.  It should be on the Apple and Windows Phone Stores later this week!<br>
<br>
<h3>Wiki rework</h3>
We shall be reworking the wiki page and using that information in the report.<br>
<br>
<br>
<h3>The Report and App Development</h3>
The report for this project will be available to download once it is complete in the next 5 weeks.  This report will be submitted to the CREST organisation for review and approval for Gold.  Once this has been completed the CMD Enterprise organisation will ramp up application development and start publishing to all platforms, including the following:<br>
<ul><li>Windows Phone 7.8<br>
</li><li>Windows Phone 8<br>
</li><li>iOS 5 on wards<br>
</li><li>Android 3.0 on wards</li></ul>

Please keep an I out on the windows phone store for new apps from us!  The latest of all is the <b>A+ League Guide</b> which has now been on the store for one week and received hundreds of downloads while it is free.  We shall be pricing it shortly and offering a trial version.  Get the full version now!!<br>
<br>
<br>
<h3>CMD apps</h3>
The CMD enterprises team has now moved onto application development for the Windows Phone 8 Store.  Please download these high quality applications that we are developing.  A new League of Legends application will be available shortly along with a Raspberry Pi Ultimate Guide and Information application.  We use the apps developed by the CMD Enterprise team on a daily basis.  See link below for apps that have been released.<br>
<br>
<a href='http://www.windowsphone.com/en-au/search?q=cmd%20enterprises'>http://www.windowsphone.com/en-au/search?q=cmd%20enterprises</a>

Enjoy.<br>
<br>
28/5/13<br>
<br>
<br>
<h3>Original Video Files</h3>
The original video files from the Raspberry Pi Camera have been uploaded and are available for download and analysis.  Links below:<br>
<br>
1080p/30:  <a href='https://docs.google.com/file/d/0B2c1yWFxK5gIeG1Da3JkZERYaUE/edit?usp=sharing'>https://docs.google.com/file/d/0B2c1yWFxK5gIeG1Da3JkZERYaUE/edit?usp=sharing</a>

720p/60:  <a href='https://docs.google.com/file/d/0B2c1yWFxK5gIRUlTM011WDVab1E/edit?usp=sharing'>https://docs.google.com/file/d/0B2c1yWFxK5gIRUlTM011WDVab1E/edit?usp=sharing</a>

I relise that the 720p/60 video maybe only 30 fps but this is a software flaw that I cannot fix.  I will upload new footage when this problem is rectified by the RPi Foundation.<br>
<br>
27/5/13<br>
<br>
<br>
<h3>New Python Module</h3>
The NEW!  Raspberry Pi GPIO Python Module has been released.  This means that the robot no-longer needs to have an Arduino on-board.  This creates higher power inefficiency and means that we remove any serial complications that we may have had.<br>
<br>
18/5/13<br>
<br>
<br>
<h3>Camera Board Arrived</h3>
Thanks to the early arrival of the Raspberry Pi Camera add-on, this project can continue to include the camera as the primary video stream.  @wallarug will get to work on this over the next few weeks.  Keep posted for future updates and events.<br>
<br>
14/05/13<br>
<br>
<h3>Video of Camera Working at 1080p/30</h3>
<a href='http://www.youtube.com/watch?feature=player_embedded&v=wW1VeV66ugk' target='_blank'><img src='http://img.youtube.com/vi/wW1VeV66ugk/0.jpg' width='425' height=344 /></a>