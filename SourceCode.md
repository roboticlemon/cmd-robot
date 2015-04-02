# Introduction #

Throughout this project we have been posting many different pieces of information on the wiki and on the Downloads page.  All the different names can get confusing.  On this page is a list of all the different (completed) pieces of software and some usage instructions.


## Python 2.7 ##

### Control Module BETA 1.6.3c .py ###

The first program is the main client that is used as a stand-alone in a IDLE shell.  This version has added comments and does not function any differently than 1.6.3.  It includes all developer tools as well.

```python2.7

print "*************************"        ###########################################
print "*Module version Beta 1.6*"        #     #####     ##    ##      #####       #
print "*Standby for imports....*"        #   ####      #    ##    #     ####  ###  #
print "*************************"        #   ##       ###  ####  ###    ####  #### #
print "                         "        #   ###      ###  ####  ###    ####  ###  #
import pygame                            #     #####  ###  ####  ###    ####       #
import socket                            ###########################################
import sys                               #Revision number: 2                       #
import os                                ###########################################
from time import gmtime, strftime, sleep
from pygame.locals import *

##########################################
# All Variables used in script being     #
#  set to zero so that it is recognised  #
#   by the except statements.            #
##########################################

init = 0            #
question_one = 0
question_two = 0    #
question_three = 0
network_one = 0
network_two = 0
network_value = 0
motor_a =0
motor_b = 0
a = 0               #
b = 0               #
x = 0
y = 0
manual_input = 0
debug_value = 0     #
i = 0
motor_a_prev = 0    #
motor_b_prev = 0    #
dir_y_prev = 0      #
servo_prev = 0      #
dir_y = 0
connection = 0
robot_detection = 0 #
servo = 90

#################################
# Pygame Mixer / Music Modules! #
#################################

pygame.mixer.init()
pygame.mixer.music.load('WELCOME BACK.wav')  #NOTE: one must have the sound file to make this work.
pygame.mixer.music.play()

############################
# Declearing sendcommmand. #
############################

# This is for sending all values onto the TCP Server.

def sendcommand(): # took out servo, motor_a,motor_b,dir_y
byte1 = chr(int(motor_a))
byte2 = chr(int(motor_b))
byte3 = chr(int(dir_y))
##    byte4 = chr(int(servo))
sock.send(byte1+byte2+byte3) # took out byte4

##################
#Asset Detection!#
##################

# Checks whose computer is being used.  These directories were manually made.
#  No users called Cian or Tom, just an empty folder.

if os.path.exists("C:\Users\Tom"):
commander_name = "Ingram"
elif os.path.exists("C:\Users\Cian"):
commander_name = "Byrne"
else:
commander_name = ""

# Gets the time.
time = strftime("%H:%M:%S")

# Checks what OS one is using and then works out which version.

os_type = os.name
if os_type == "nt":
os_type = "Windows"
if os.path.exists("C:\Windows\DesktopTileResources"):
os_name = "8"
kernel_version = str("6.2")
else:
os_name = "7"
kernel_version = str("6.1")

else:
os_type = "OSX"
os_name = "10.8"
kernel_version = str("XNU") #Will make searchable if command post switches so Linux/OSX

#############################
#  DIALOGUE OUTPUT ON START #
#############################

print ("Welcome back Commander " + commander_name)
print ("You are running on " + os_type + " " + os_name + " with kernel version " + kernel_version)
print " "
print ("The current time is " + time)
print " "


##########################################
# Manual functionality specification     #
# Ingram & Byrne's idea                  #
##########################################

# This section askes the user a series of questions before deciding which robot to use.
#  This takes a while.

try:
robot_detection = raw_input("Which Robot do you wish to control? (overwatch = '1' / recon = '2' / butterfly = '3'): ")

while robot_detection != '1' or robot_detection != '2' or robot_detection == '3':
if robot_detection == '3':
print 'Support for CMDbutterfly will be coming in a later release.  Please select another option from the ones provided. '
elif robot_detection == '1' or robot_detection == '2' or robot_detection == '50':
break
else:
print 'Enter a valid value! '
robot_detection = raw_input("Which Robot do you wish to control? (overwatch = '1' / recon = '2' / butterfly = '3'): ")


if robot_detection == '1':
robot_detection = 'CMDoverwatch'
elif robot_detection == '2':
robot_detection = 'CMDrecon'
elif robot_detection == '50':
robot_detection = 'home'

print " "
print  "Controlling " +robot_detection
print " "
question_one = raw_input("Would you like to use Default Settings? (y/n): ")
if question_one == "y":
question_two = "y"
question_three = "y"
network_value = "y"
#debug_value = "y"
i = "pos"

if question_one != "y":
network_value = "n"
if question_one != "n":
while question_one != "y" and question_one != "n":
print "Please enter a valid value"
question_one = raw_input("Would you like to start both the TCP client and Joystick? (y/n): ")
if question_one == "y":
question_two = "y"
question_three = "y"
elif question_one == "n":
break
question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")

while question_two != "y" and question_two != "n":
if question_two == "y" or question_two == "n":
break
print "Please enter a valid value"
question_two = raw_input("Would you like to enable TCP client for this sesson? (y/n): ")

question_three = raw_input("Would you like to enable the Joystick Controller? (y/n): ")
while question_three != "y" and question_three != "n":
if question_three == "y" or question_three == "n":
break
print "Please enter a valid value"
question_three = raw_input("Would you like to enable the Joystick Controller? (y/n): ")


############################
#Joystick Detection Script!#
############################

if question_three == "y":
pygame.init()
joycount = pygame.joystick.get_count()

if joycount == 0:
print "                                                                      "
print "**********************************************************************"
print "* [ WARNING ]           No joystick detected!            [ WARNING ] *"
print "*                                                                    *"
print "*                   Restart module with joystick!                    *"
print "*                                                                    *"
print "* [ WARNING ]           Module halt in TIME-5            [ WARNING ] *"
print "**********************************************************************"
sleep(5)
sys.exit("No joystick found!")
else:
print " "
print "[ SUCCESS ] Joystick Detected! [ SUCCESS ] "
j = pygame.joystick.Joystick(0)
j.init()
print " "
print " ************************************************ "
print ' * Initialized Joystick : %s' % j.get_name() + " * "
print " ************************************************ "
else:
print "                                                                          "
print "**************************************************************************"
print "*                                                                        *"
print "* [ WARNING ]  Manual input method will now be activated!  [ WARNING ]   *"
print "*                                                                        *"
print "**************************************************************************"
manual_input = 1



#########################
# TCP client is  below. #
#########################

######################################
# Check for TCP connection settings. #
######################################

while question_two == "y":
if network_value == "n":
print " "
print " "
network_one = raw_input("Would you like to use a pre-set IP address? ('n' or 'adhoc'/'local') : ")
while network_one != "n" and network_one != "adhoc" and network_one != "local":
print "Please enter a valid value"
network_one = raw_input("Would you like to use a pre-set IP address? ('n' or 'adhoc'/'local') : ")
if network_one == "n" or network_one == "adhoc" or network_one == "local":
break
if network_one == "adhoc":
HOST, PORT = "192.168.12.37", 8999
sockname = robot_detection
elif network_one == "local":
HOST, PORT = 'localhost', 9999
sockname = str(socket.gethostname())
elif network_one == "n":
HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. 192.168.12.1): ")
PORT = input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")
sockname = robot_detection
elif network_value == "y":
if robot_detection == 'CMDoverwatch':
HOST, PORT = "10.0.0.1", 8999
sockname = "CMDoverwatch"
elif robot_detection == 'CMDrecon':
HOST, PORT = "10.0.0.50", 9999
sockname = "CMDrecon"
elif robot_detection == 'home':
HOST, PORT = "192.168.12.37", 8999
sockname = "HOME DEVICE!"

connection = 0
connection_attempt = 1
con_attempted = 0
while connection == 0:
print " "
print "[ ALERT ]  Stand by for TCP connection on " + str(HOST) + ":" + str(PORT)+ "!  Attempt: " + str(connection_attempt) + "  [ ALERT ]"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
sock.connect((HOST, PORT)) #'''Added in a try command for unsucessful TCP connection'''
print " "
print "[ ALERT ]   Connected to " +str(sockname)+" @ "+ str(HOST) + ":" + str(PORT)+"  [ ALERT ]   "
connection = 1

except:
#print " "
print "[ ALERT ]  Unable to connect to " + HOST +", please check your connection!   [ ALERT ]"
connection_attempt = connection_attempt + 1
sleep(5)
if connection_attempt > 2 and con_attempted == 0:
print " "
con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")
con_attempted = 1
while con_attempt != "y" and con_attempt != "n":
print "Please input a valid value!"
con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")

if con_attempt == "n":
HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. '192.168.12.1'): ")
PORT = input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")


if connection_attempt > 5:
print "[ WARNING ]  Connection attempts have failed, the script will now exit!  [ WARNING ] "
sleep(3)
sys.exit("Connection Failed!")
break #Discovered flaw, once completed that section would continue the while loop!

else:
print " "
print "[ WARNING ]  No TCP Client this sesson!  [ WARNING ] "
except KeyboardInterrupt:
if question_two == "y":
sock.shutdown(socket.SHUT_RDWR)
sock.close()
sys.exit("Closing Application...")


#########################################
# The mode that you want to enter which #
#  can be one of the following:         #
#########################################

try:
if question_one != "y":
if str(question_three) == "y":
print " "
i = raw_input("What do you want to detect? (button/pos/all): ")
elif str(question_three) == "n":
print " "
debug_value = raw_input("Do you want to enter debug mode? (y/n): ")
else:
print "Enter a correct value next time!"
sys.exit("Value Error!")
except KeyboardInterrupt:
if question_two == "y":
sock.shutdown(socket.SHUT_RDWR)
sock.close()
sys.exit("Closing Application...")


######################################
#                                    #
#       D E B U G   M O D E          #
#                                    #
#      Advanced out of ALPHA         #
######################################

#  Not used very offen / at all.
try:
if debug_value == "n":
print " Loading WASD Full Speed Control..."
pygame.init()
screen = pygame.display.set_mode((64, 64))
pygame.display.set_caption('WASD Control of CMD-ROBOT')
pygame.mouse.set_visible(0)
done = False
while not done:
for event in pygame.event.get():
if (event.type == KEYUP):
if (event.key == K_a):
print "Moving Left!"
motor_b = 255
motor_a = 0
dir_y = 1
servo = 90
elif (event.key == K_s):
print "Moving Backwards!"
dir_y = 2
motor_a = 255
motor_b = 255
servo = 90
elif (event.key == K_d):
print "Moving Right!"
dir_y = 1
motor_b = 0
motor_a = 255
servo = 90
elif (event.key == K_w):
print "Moving Forwards!"
dir_y = 1
motor_a = 255
motor_b = 255
servo = 90
elif (event.key == K_ESCAPE):
done = True
else:
motor_a = 0
motor_b = 0
if question_two == "y":
sendcommand()
print (motor_a,motor_b)
except KeyboardInterrupt:
if question_two == "y":
sock.shutdown(socket.SHUT_RDWR)
sock.close()
sys.exit("Closing Application...")

try:
if debug_value == "y":
print " "
print "Welcome to Debug mode for CMD robots...Use with caution!!! "
print "Loading... "
sleep(3)
print " "
print "[ ALERT ]  Script Loaded Successfully!  [ ALERT ]  "
print " "
print " ******************* "
print " * BEGIN DEBUGGING * "
print " ******************* "
while True:
print " "
motor_a = input("LEFT MOTOR: Enter value between -255 and 255: ")
motor_b = input("RIGHT MOTOR: Enter value between -255 and 255: ")
if motor_a < 0 and motor_a > -256 or motor_b < 0 and motor_b > -256:
dir_y = 2
##                motor_a = 255 - abs(motor_a)
motor_a = abs(motor_a)
##                motor_b = 255 - abs(motor_b)
motor_b = abs(motor_b)
print "Going Backwards!"
if question_two == "y":
sendcommand()
print "Sent to server!"
elif motor_a >= 0 and motor_a < 256 or motor_b >= 0 and motor_b < 256:
dir_y = 1
motor_a = abs(motor_a)
motor_b = abs(motor_b)
print "Going Forwards!"
if question_two == "y":
sendcommand()
print "Sent to server!"
elif motor_a == "" or motor_b == "": # Will work once we change input to raw_input otherwise we get an error!
motor_a = 0
motor_b = 0
dir_y = 1
if question_two == "y":
sendcommand()
print "Reset values command sent to server!"
else:
print "Number not in range, value not sent to server"
print "Not sent to TCP Server!"
print (motor_a, motor_b)
except KeyboardInterrupt:
if question_two == "y":
sock.shutdown(socket.SHUT_RDWR)
sock.close()
sys.exit("Closing Application...")





#########################################################
#  MAIN CLIENT SCRIPT TO CONTROL ROBOTS WITH JOYSTICK.  #
#########################################################

try:
while i == "pos":
if question_two == "y":
sockname = str(sockname)
else:
sockname = "nothing"
init = 1
if init == 0:
print " "
print "[ WARNING ]  Initiating Control of " + str(sockname) + " in...  [ WARNING ] "
print " "
print " ************************************* "
print " "
print " * Initiated Control of " + str(sockname) + "!"
print " "
print " ************************************* "
init = init + 1
sleep (1.5)


pygame.event.pump()
x = j.get_axis(0)
x = round(x,4)
y = j.get_axis(1)
y = round(y,4)
z = j.get_axis(2)
z = round(z,1)
#print(x,y,z)

if y < 0:               ############################
y = abs(y)          #New Y-axes inversion code!#
elif y > 0:             ############################
y = y*-1

#############################################
# Formulas for working out the speed of the #
# motor in certain areas of the Joystick!   #
#############################################

f = 1
sy = f*(y)
sx = f*(x)


#############################################
## Joystick Control Registry and Conversion!#
#############################################

#if j.get_button(0):
#if j.get_name() != 'wide':
if x == 0:
a = abs(sy)
b = abs(sy)
elif y > 0:
if x > 0 and y <= x:
a = abs(x)
b = 0
elif x > 0 and y > x:
a = abs(sy)
b = abs(sy) - abs(x)
elif x < 0 and y <= -x:
b = abs(x)
a = 0
elif x < 0 and y > -x:
b = abs(sy)
a = abs(sy) - abs(x)

elif y == 0 and x != 0:
if x < 0:
a = 0
b = abs(sx)
elif x > 0:
a = abs(sx)
b = 0
elif y < 0:
if x > 0 and y >= -x:
a = abs(x)
b = 0
elif x > 0 and y < -x:
a = abs(sy)
b = abs(sy) - abs(x)
elif x < 0 and y >= x:
a = 0
b = abs(x)
elif x < 0 and y < x:
a = abs(sy) - abs(x)
b = abs(sy)
#if j.get_name() == 'wide':
#a = x
#b = x
else:
a = 0
b = 0


######################################
## PWM convertion for AnalogueWrite()#
######################################

PWM = 255
a = PWM*a
a = round(a, 1)
b = PWM*b
b = round(b, 1)

###################################
# Arduino Varibles Decleared Here!#
###################################

motor_a = a
motor_b = b

####################################
# NEW: Single PWM Channel LOW fix! #
####################################
if robot_detection == 'CMDoverwatch' or robot_detection == 'home':
if y < 0:
y = 2                # Backwards
else:
y = 1                # Forewards
dir_y = y
elif robot_detection == 'CMDrecon':
if y < 0:
y = 2                # Backwards
motor_a = 255 - abs(motor_a)
motor_a = abs(motor_a)
motor_b = 255 - abs(motor_b)
motor_b = abs(motor_b)
else:
y = 1                # Forewards
dir_y = y
###############################
#  NEW: Servo Control Script! #
###############################

# Commented due to fire started.

##        servo_control = 45*abs(x)
##
##        if x > 0:
##            servo = 90 + servo_control
##        elif x < 0:
##            servo = 90 - servo_control
##        else:
##            servo = 90
##        servo = round(servo, 0)


##########################################
# Sends data ONLY when data is different!#
##########################################

if question_two == "y":
if motor_a != motor_a_prev:
sendcommand()
elif motor_b != motor_b_prev:
sendcommand()
elif dir_y != dir_y_prev:
sendcommand()
##            elif servo != servo_prev:
##                sendcommand()


motor_a_prev = motor_a
motor_b_prev = motor_b
dir_y_prev = dir_y
##            servo_prev = servo


####################################
# Printing Output - Only used in   #
# development of Joystick Control. #
####################################

print (int(a),int(b)) # Comment this line for no speed output.

except KeyboardInterrupt:
if question_two == "y":
sock.shutdown(socket.SHUT_RDWR)
sock.close()
sys.exit("Closing Application...")

#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################


##################
#CUSTOM FUNCTIONS#  Currently unstable, to make usable in coming updates
##################


while i == "button":
pygame.event.pump()
if j.get_button(1):
print "Left"
if j.get_button(0):
print "Kill"
if j.get_button(2):
print "Right"

###################################################

while i == "speed":
print"currently in progress"
x = 0.4
y = 0.5
f = 100
sy = f*abs(y)
print sy


###################################################


while i == "all":
pygame.event.pump()
y = j.get_axis(1)
y = round(y,2)
x = j.get_axis(0)
x = round(x,2)
z = j.get_axis(2)
z = round(z,1)
if j.get_button(0):
b0 = " Kill"
else:
b0 = ""
if j.get_button(1):
b1 = " Left"
else:
b1 = ""
if j.get_button(2):
b2 = " Right"
else:
b2 = ""
print(str(x) + "," + str(y) + "," + str(z) + b0 + b1 + b2)

'''CMD Official Comment ART

#####################################
###     #####    ##    #####      ###
##  ########   #    #   ####  ###  ##
##  ########  ###  ###  ####  #### ##
##  ########  ###  ###  ####  ###  ##
###     ####  ###  ###  ####      ###
#####################################
'''
endstatement = raw_input("You have reached the end of the script! (exit/ *) ")
if endstatement == "exit":
sys.exit("End of script!")

```


### TCP debug! Version 2.0.1 ###
This is the TCP Server that we connect to via the client script.  It runs on the Raspberry Pi and is always on - even if connection is lost (thanks to developer's improvements).

```


print "Welcome to TCP debug! Version 2.0.1"
from time import sleep
import sys
import os
import socket
'''
TCP Server gets hostname from local machine and uses the hostname to
get the IP address of the Machine.

This is so that it does not matter what machine you are running the script
on, which means that you don\'t need to change anything. :D

Cian Byrne
'''

try:
while True:
def closeall():
print "[ALERT]  Closing shell...  [ALERT]"
if enableserial == 1:
sendcommand()
sleep(0.125)
ser.close()
c.shutdown(socket.SHUT_RDWR)
c.close
sleep(1)
sys.exit("Application forcibly halted! - Level 2")

def sendcommand():
byte1 = chr(0)  #motor L
byte2 = chr(0)  #motor R
byte3 = chr(1)  #direction y
# byte4 = chr(int(90)) #servo
msg = (byte1+byte2+byte3) #took out byte4
ser.write(msg)

##############################################
# Change to '1' to enable serial connection. #
##############################################

enableserial = 1

#################
# Server Setup. #
#################

s = socket.socket()
#HOST = "192.168.12.46"     # For Debugging
#HOST = "10.0.0.1"
HOST = "localhost"
PORT = 9999                 # Reserve a port for your service.


######################################
# Setup Serial interface if enabled. #
######################################

if enableserial == 1:
import serial
#DEVICE = '/dev/ttyACM0' # the arduino serial interface (use dmesg when connecting)
DEVICE = 'COM4'
#DEVICE = '/dev/ttyAMA0'  #Raspberry Pi Serial Port RX/TX
BAUD = 9600
ser = serial.Serial(DEVICE, BAUD)
sendcommand()
#################
# Start Server. #
#################

try:
print "Server started on", str(HOST) + ":" + str(PORT)
print 'Waiting for clients...'

s.bind((HOST, PORT))        # Bind to the port
s.listen(1)         # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
print "Standby for data receive!"

while True:
msg = c.recv(3) # get 3 bytes from the TCP connection
if enableserial == 1:
ser.write(msg)  # write the 3 bytes to the serial interface
print "Data written to Serial Device!"
############################################
# loop back to top of script and close all #
#  connections if connection is lost.      #
############################################

if msg == "":
if enableserial == 1:
sendcommand()
sleep(1.5)
ser.close()
c.shutdown(socket.SHUT_RDWR)
c.close()
print "Lost connection with"+ str(addr) +"! Restarting server..."
sleep(2)
break

except KeyboardInterrupt:
sendcommand()
sleep(0.5)
c.close()
ser.close()
sys.exit("Forcibly halted at level 1")
except KeyboardInterrupt:
closeall()


## Depreciated code is below.  Please use only in later releases:
#  This is for the hostname look-up for IP address.
#       #hostname = socket.gethostname()
#host = str(socket.gethostbyname_ex(hostname)[2]).strip("['']")
#HOST = str(host)
#
#
#
#
#
#
#


```

## Ardunio Sketches ##
This is installed onto the Arduino and controls the PWM signal to the motors.  There is two versions, one for CMDoverwatch the other for CMDrecon.  See below:

#### CMD recon ####
I don't think this one works with the python script.  You will have to use the GUI vb.NET program.

```

/*
 * Robot Motor Controller script with PWM speed control - Duel Channel
 *   Control with support for 'Pivot'
 *
 *  By Cian Byrne
 *   CMD Enterprises 2013
 *
 * WARNING: ONLY USE THIS SCRIPT WITH CMDrecon!!
 */
//---------------------- variables
int motorL[] = {3, 5};
int motorR[] = {11, 6};
int ledPin = 13;
int Byte1 = 0;  //for incoming serial data
int Byte2 = 0;  //for incoming serial data
int Byte3 = 0;  //for incoming serial data
int motor_a = 0;
int motor_b = 0;
int dir_y = 0;


void setup() {
Serial.begin(9600);  // opens serial port, sets data rate at 9600bps
int i;
for(i = 0; i < 2; i++){
pinMode(motorL[i], OUTPUT);
pinMode(motorR[i], OUTPUT);
pinMode(ledPin, OUTPUT);
}

}

void loop() {
digitalWrite(ledPin, HIGH);

if(Serial.available()==3)
{
  Byte1 = Serial.read(); // Incoming data from Serial connection
  motor_a = int(Byte1);
  Byte2 = Serial.read(); // Incoming data from Serial connection
  motor_b = int(Byte2);
  Byte3 = Serial.read(); // Incoming data from Serial connection
  dir_y = int(Byte3);
  
  if (dir_y == 1) {  //Motor Forwards and Single motor Turning
  digitalWrite(motorL[0], LOW);
  digitalWrite(motorL[1], HIGH);
  digitalWrite(motorR[0], LOW);
  digitalWrite(motorR[1], HIGH);
  analogWrite(5, motor_a);
  analogWrite(6, motor_b);
  }
  else if (dir_y == 2) { //Motor Backwards
  digitalWrite(motorL[0], HIGH);
  digitalWrite(motorL[1], LOW);
  digitalWrite(motorR[0], HIGH);
  digitalWrite(motorR[1], LOW);
  analogWrite(3, motor_a);
  analogWrite(11, motor_b);
  }
  else if (dir_y == 3){ //Pivot Right
  digitalWrite(motorL[0], HIGH);
  digitalWrite(motorL[1], LOW);
  digitalWrite(motorR[0], LOW);
  digitalWrite(motorR[1], HIGH);
  analogWrite(3, motor_a);
  analogWrite(6, motor_b);
  }
  else if (dir_y == 4){ //Pivot Right
  digitalWrite(motorL[0], LOW);
  digitalWrite(motorL[1], HIGH);
  digitalWrite(motorR[0], HIGH);
  digitalWrite(motorR[1], LOW);
  analogWrite(5, motor_a);
  analogWrite(11, motor_b);
}
}
}

```

#### CMD overwatch ####

I don't think this one works with the python script.  You will have to use the GUI vb.NET program.

```
/*
 * Robot Motor Controller script with PWM speed control
 */
//---------------------- Motors
int motorLHigh = 4;
int motorLLow = 2;
int motorLPWM = 5;
int motorRHigh = 7;
int motorRLow = 8;
int motorRPWM = 6;
int ledPin = 13;
int Byte1 = 0;  //for incoming serial data
int Byte2 = 0;  //for incoming serial data
int Byte3 = 0;  //for incoming serial data
int motor_a = 0;
int motor_b = 0;
int dir_y = 0;


void setup() {
Serial.begin(9600);  // opens serial port, sets data rate at 9600bps
pinMode(motorLPWM, OUTPUT);
pinMode(motorRPWM, OUTPUT);
pinMode(motorRHigh, OUTPUT);
pinMode(motorRLow, OUTPUT);
pinMode(motorLHigh, OUTPUT);
pinMode(motorLLow, OUTPUT);
pinMode(ledPin, OUTPUT);
}


void loop() {
digitalWrite(ledPin, HIGH);

if(Serial.available()==3)
{
  Byte1 = Serial.read(); // Incoming data from Serial connection
  motor_a = int(Byte1);
  Byte2 = Serial.read(); // Incoming data from Serial connection
  motor_b = int(Byte2);
  Byte3 = Serial.read(); // Incoming data from Serial connection
  dir_y = int(Byte3);
  
  if (dir_y == 1) {  //Motor Forwards and Single motor Turning
  digitalWrite(motorLLow, LOW);
  digitalWrite(motorLHigh, HIGH);
  digitalWrite(motorRLow, LOW);
  digitalWrite(motorRHigh, HIGH);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }
  else if (dir_y == 2) { //Motor Backwards
  digitalWrite(motorLLow, HIGH);
  digitalWrite(motorLHigh, LOW);
  digitalWrite(motorRLow, HIGH);
  digitalWrite(motorRHigh, LOW);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);

  }
  else if (dir_y == 3) {  //Pivot Right
  digitalWrite(motorLLow, HIGH);
  digitalWrite(motorLHigh, LOW);
  digitalWrite(motorRLow, LOW);
  digitalWrite(motorRHigh, HIGH);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }  
  else if (dir_y == 4) {  //Pivot Left
  digitalWrite(motorLLow, LOW);
  digitalWrite(motorLHigh, HIGH);
  digitalWrite(motorRLow, HIGH);
  digitalWrite(motorRHigh, LOW);
  analogWrite(motorLPWM, motor_a);
  analogWrite(motorRPWM, motor_b);
  }
  }
  
}

```

# GUI Programs #

After we had completed the python script to the best of our ability, we decided to try our hand at some vb.net and XAML.  This produced one of the two GUI programs that we made.  One problem with the XAML version was that it was written in Ironpython (read more on [GUI page](https://code.google.com/p/cmd-robot/wiki/GUI) which used many different libraries and files to work and was not very stable.  Below is that particular set-up.

## CMD ROBOT Control System - Beta Release 3 ##
### Ironpython ###
This ran behind the XAML file. and was called: CMDrobotcontrolmoduleapp.py .  You can download all this source from

```
import wpf
import clr
import os
import sys
from System.Diagnostics import Process
from time import gmtime, strftime, sleep
from System.Windows.Controls import Image
from System.Environment import OSVersion

from System.Windows import Application, Window, MessageBox   # This Line works when un-commented

class StartWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'CMDrobotcontrolmoduleapp.xaml')
        self.IPaddress_TextBox.Text = 'Type IP address'
        self.Port_TextBox.Text = 'Type Port Number'
        self.JoystickEnable_CheckBox.IsChecked = True
        self.DebugEnabled_CheckBox.IsChecked = False
        self.TCPEnabled_CheckBox.IsChecked = True
        self.dev_CheckBox.IsChecked = True
        if os.path.exists("C:\Users\Tom"):
            self.user = "Commander Ingram"
            self.User_TextBox_New.Text = self.user
            self.CMDrecon_radiobutton.IsChecked = True
        elif os.path.exists("C:\Users\Cian"):
            self.user = "Commander Byrne"
            self.User_TextBox_New.Text = self.user
            self.CMDoverwatch_radiobutton.IsChecked = True
        else:
            self.User_TextBox_New.Text = "Unknown"

    def Start_Button_Click(self, sender, e):
        self.Port = self.Port_TextBox.Text
        self.IPaddress = self.IPaddress_TextBox.Text
        if self.JoystickEnable_CheckBox.IsEnabled == True:
            self.Joystick = 'y'
        if self.JoystickEnable_CheckBox.IsChecked == False:
            self.Joystick = 'n'
        if self.DebugEnabled_CheckBox.IsChecked == True:
            self.Debug = 'y'
        if self.DebugEnabled_CheckBox.IsChecked == False:
            self.Debug = 'n'
        if self.TCPEnabled_CheckBox.IsChecked == True:
            self.TCP = 'y'
        if self.TCPEnabled_CheckBox.IsChecked == False:
            self.TCP = 'n'
        self.file = open('details.txt', 'w')
        self.file.write(self.Port+'\n'+self.IPaddress+'\n'+self.CMDrobot+'\n'+self.TCP+'\n'+self.Joystick+'\n'+self.Debug+'\n')
        self.file.close()
        Process.Start('python.exe', 'ControlModuleBeta1.6.6.py')
     
    def Info_Button_Click(self, sender, e):
        time = strftime("%H:%M:%S")
        major = str(OSVersion.Version.Major)
        minor = str(OSVersion.Version.Minor)
        kernel = major + "." + minor
       # opsys = "Unknown"
        if kernel == "6.2":
            opsys = "Windows 8"
        elif kernel == "6.1":
            opsys = "Windows 7"
        elif kernel == "6.0":
            opsys = "Windows Vista"
        else:
            opsys = "Windows XP"
        MessageBox.Show("Information about your PC: \n \n" + "OS Version = " + opsys + "\nKernel Version = " + kernel, "PC Information")

    def Close_Button_Click(self, sender, e):
        Application.Current.Shutdown()
    
    def CMDrecon_radiobutton_Checked(self, sender, e):
        self.Port_TextBox.Text = "9999"
        self.IPaddress_TextBox.Text = "10.0.0.10"
        self.CMDrobot = 'CMDrecon'
    
    def CMDoverwatch_radiobutton_Checked(self, sender, e):
        self.Port_TextBox.Text = "8999"
        self.IPaddress_TextBox.Text = "10.0.0.1"
        self.CMDrobot = 'CMDoverwatch'

    def Port_TextBox_GotFocus(self, sender, e):
        self.Port_TextBox.Text = ''

    def IPaddress_TextBox_GotFocus(self, sender, e):
        self.IPaddress_TextBox.Text = ''

    def IPaddress_TextBox_TextChanged(self, sender, e):
        pass
    
    def Port_TextBox_TextChanged(self, sender, e):
        pass
   
    def User_TextBox_New_TextChanged(self, sender, e):
        pass
    
    def btn_test_Click(self, sender, e):
        MessageBox.Show("Welcome " + self.user + " to the Dev console, in future this will launch the Black Frost Console!", "Dev Console Alert" )
    
    def dev_CheckBox_Checked(self, sender, e):
        self.btn_test.IsEnabled = True

    def dev_CheckBox_UnChecked(self, sender, e):
        self.btn_test.IsEnabled = False
    
    def JoystickEnable_CheckBox_Checked(self, sender, e):
        self.DebugEnabled_CheckBox.IsChecked = False
            
    def DebugEnabled_CheckBox_Checked(self, sender, e):
        self.JoystickEnable_CheckBox.IsChecked = False
            
    def TCPEnabled_CheckBox_Checked(self, sender, e):
        pass

if __name__ == '__main__':
    Application().Run(StartWindow())
    

```

### Python ###
This ran on the press of the button on the XAML page.  It is the enhanced version of Control Module Beta 1.6.3 for use with Ironpython.  It is called Control Module Beta 1.6.6.py  and is downloadable in package.

```
print "*************************"        ###########################################
print "*Module version Beta 1.6*"        #     #####     ##    ##      #####       #
print "*Standby for imports....*"        #   ####      #    ##    #     ####  ###  #
print "*************************"        #   ##       ###  ####  ###    ####  #### #
print "                         "        #   ###      ###  ####  ###    ####  ###  #
import pygame                            #     #####  ###  ####  ###    ####       #
import socket                            ###########################################
import sys                               #Revision number: 2                       # 
import os                                ###########################################
from time import gmtime, strftime, sleep
from pygame.locals import *
##########################################
# All Variables used in script being     #
#  set to zero so that it is recognised  #
#   by the except statements.            #
##########################################

init = 0            #
network_one = 0
network_two = 0
network_value = 0
motor_a =0
motor_b = 0
a = 0               #
b = 0               #
x = 0
y = 0
manual_input = 0
debug_value = 0     #
i = 0
motor_a_prev = 0    #
motor_b_prev = 0    #
dir_y_prev = 0      #
servo_prev = 90      #
dir_y = 0
connection = 0
robot_detection = 0 #
servo = 90

##########################################################################
#  NEW: GUI IronPython Features.  This area is for opening a file        #
#    which has configuration settings in it.  Line by Line Explained:    #
##########################################################################

configfile = open('details.txt', 'r')
PORTA = configfile.readline().strip('\n')
HOSTA = configfile.readline().strip('\n')
robot_detection = configfile.readline().strip('\n')

tcp_enabled = configfile.readline().strip('\n')
joy_enabled = configfile.readline().strip('\n')
debug_enabled = configfile.readline().strip('\n')

##HOSTA = "10.0.0.39"
##PORT = 9999
##robot_detection = "CMDrecon"
##tcp_enabled = "y"
##joy_enabled = "y"
##debug_enabled = "n"



print 'PORT: ' +PORTA
print 'HOST: '+HOSTA
print 'Robot: '+robot_detection
print 'Joystick enabled: '+joy_enabled
print 'Debug enabled: '+debug_enabled
print 'TCP enabled: '+tcp_enabled
sleep(3)

#################################
# Pygame Mixer / Music Modules! #
#################################


############################
# Declearing sendcommmand. #
############################

def sendcommand(): # took out servo, motor_a,motor_b,dir_y
    byte1 = chr(int(motor_a))
    byte2 = chr(int(motor_b))
    byte3 = chr(int(dir_y))
    #byte4 = chr(int(servo))
    sock.send(byte1+byte2+byte3) # took out byte4

##################
#Asset Detection!#
##################




##########################################
# Manual functionality specification     #
# Ingram & Byrne's idea                  #
##########################################

try:


    ############################
    #Joystick Detection Script!#
    ############################

    if joy_enabled == "y":
        pygame.init()
        joycount = pygame.joystick.get_count()

        if joycount == 0:
            print "                                                                      "
            print "**********************************************************************"
            print "* [ WARNING ]           No joystick detected!            [ WARNING ] *"
            print "*                                                                    *"
            print "*                   Restart module with joystick!                    *"
            print "*                                                                    *"
            print "* [ WARNING ]           Module halt in TIME-5            [ WARNING ] *"
            print "**********************************************************************"
            sleep(5)
            sys.exit("No joystick found!")
        else:
            print " "
            print "[ SUCCESS ] Joystick Detected! [ SUCCESS ] "    
        j = pygame.joystick.Joystick(0)
        j.init()
        print " "
        print " ************************************************ " 
        print ' * Initialized Joystick : %s' % j.get_name() + " * "
        print " ************************************************ "
    else:
        print "                                                                          "
        print "**************************************************************************"
        print "*                                                                        *"
        print "* [ WARNING ]  Manual input method will now be activated!  [ WARNING ]   *" 
        print "*                                                                        *"
        print "**************************************************************************"
        manual_input = 1



    #########################
    # TCP client is  below. #
    #########################

    ######################################
    # Check for TCP connection settings. #
    ######################################

    while tcp_enabled == "y":
        HOST, PORT = str(HOSTA), int(PORTA)
        sockname =  robot_detection
        connection = 0
        connection_attempt = 1
        con_attempted = 0
        while connection == 0:
            print " "
            print "[ ALERT ]  Stand by for TCP connection on " + str(HOST) + ":" + str(PORT)+ "!  Attempt: " + str(connection_attempt) + "  [ ALERT ]"
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((HOST, PORT)) #'''Added in a try command for unsucessful TCP connection'''
                print " "
                print "[ ALERT ]   Connected to " +str(sockname)+" @ "+ str(HOST) + ":" + str(PORT)+"  [ ALERT ]   "
                connection = 1
            
            except:
                #print " "
                print "[ ALERT ]  Unable to connect to " + HOST +", please check your connection!   [ ALERT ]"
                connection_attempt = connection_attempt + 1
                sleep(5)
                if connection_attempt > 2 and con_attempted == 0:
                    print " "
                    con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")
                    con_attempted = 1
                    while con_attempt != "y" and con_attempt != "n":
                        print "Please input a valid value!"
                        con_attempt = raw_input("Are you sure " + str(HOST) + ":" + str(PORT) + " is your desired address? (y/n)")
                        
                    if con_attempt == "n":
                        HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. '192.168.12.1'): ")
                        PORT = input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")
                        
                    
                if connection_attempt > 5:
                    print "[ WARNING ]  Connection attempts have failed, the script will now exit!  [ WARNING ] "
                    sleep(3)
                    sys.exit("Connection Failed!")
        break #Discovered flaw, once completed that section would continue the while loop!

    else:
        print " "
        print "[ WARNING ]  No TCP Client this sesson!  [ WARNING ] "
except KeyboardInterrupt:
        if tcp_enabled == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")


#########################################
# The mode that you want to enter which #
#  can be one of the following:         #
#########################################




######################################
#                                    #
#       D E B U G   M O D E          #
#                                    #
#      Advanced out of ALPHA         #
######################################
try:
    if debug_enabled == "n" and joy_enabled == "n":
        print " Loading WASD Full Speed Control..."
        pygame.init()
        screen = pygame.display.set_mode((64, 64))
        pygame.display.set_caption('WASD Control of CMD-ROBOT')
        pygame.mouse.set_visible(0)
        done = False
        while not done:
           for event in pygame.event.get():
                if (event.type == KEYUP):
                    if (event.key == K_a):
                        print "Moving Left!"
                        motor_b = 255
                        motor_a = 0
                        dir_y = 1
                        servo = 90
                    elif (event.key == K_s):
                        print "Moving Backwards!"
                        dir_y = 2
                        motor_a = 255
                        motor_b = 255
                        servo = 90
                    elif (event.key == K_d):
                        print "Moving Right!"
                        dir_y = 1
                        motor_b = 0
                        motor_a = 255
                        servo = 90
                    elif (event.key == K_w):
                        print "Moving Forwards!"
                        dir_y = 1
                        motor_a = 255
                        motor_b = 255
                        servo = 90
                    elif (event.key == K_ESCAPE):
                        done = True
                    else:
                        motor_a = 0
                        motor_b = 0                
                    if tcp_enabled == "y":
                        sendcommand()
                    print (motor_a,motor_b)
except KeyboardInterrupt:
        if tcp_enabled == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")

try:    
    if debug_enabled == "y":
        print " "
        print "Welcome to Debug mode for CMD robots...Use with caution!!! "
        print "Loading... "
        sleep(3)
        print " "
        print "[ ALERT ]  Script Loaded Successfully!  [ ALERT ]  "
        print " "
        print " ******************* "
        print " * BEGIN DEBUGGING * "
        print " ******************* "
        while True:
            print " "
            motor_a = input("LEFT MOTOR: Enter value between -255 and 255: ")
            motor_b = input("RIGHT MOTOR: Enter value between -255 and 255: ")
            if motor_a < 0 and motor_a > -256 or motor_b < 0 and motor_b > -256:
                dir_y = 2
##                motor_a = 255 - abs(motor_a)
                motor_a = abs(motor_a)
##                motor_b = 255 - abs(motor_b)
                motor_b = abs(motor_b)
                print "Going Backwards!"
                if tcp_enabled == "y":
                    sendcommand()
                    print "Sent to server!"
            elif motor_a >= 0 and motor_a < 256 or motor_b >= 0 and motor_b < 256:               
                dir_y = 1
                motor_a = abs(motor_a)
                motor_b = abs(motor_b)
                print "Going Forwards!"
                if tcp_enabled == "y":
                    sendcommand()
                    print "Sent to server!"
            elif motor_a == "" or motor_b == "": # Will work once we change input to raw_input otherwise we get an error!
                motor_a = 0
                motor_b = 0
                dir_y = 1
                if tcp_enabled == "y":
                    sendcommand()
                    print "Reset values command sent to server!"
            else:
                print "Number not in range, value not sent to server"
                print "Not sent to TCP Server!"
            print (motor_a, motor_b)
except KeyboardInterrupt:
        if tcp_enabled == "y":
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        sys.exit("Closing Application...")





###########################################################

try:
    while joy_enabled == "y":
        if tcp_enabled == "y":
            sockname = str(sockname)
        else:
            sockname = "nothing"
        init = 1
        if init == 0:
            print " "
            print "[ WARNING ]  Initiating Control of " + str(sockname) + " in...  [ WARNING ] "
            print " "
            print " ************************************* "
            print " "
            print " * Initiated Control of " + str(sockname) + "!"
            print " "
            print " ************************************* "
            init = init + 1
            sleep (1.5)

        pygame.event.pump()
        x = j.get_axis(0)
        x = round(x,4)
        y = j.get_axis(1)
        y = round(y,4)
        z = j.get_axis(2)   
        z = round(z,1)
        #print(x,y,z)
       
        if y < 0:               ############################
            y = abs(y)          #New Y-axes inversion code!#
        elif y > 0:             ############################
            y = y*-1
            
    #############################################
    # Formulas for working out the speed of the #
    # motor in certain areas of the Joystick!   #
    #############################################

        f = 1
        sy = f*(y)
        sx = f*(x)
        

    #############################################
    ## Joystick Control Registry and Conversion!#
    #############################################

        #if j.get_button(0):
        #if j.get_name() != 'wide':
        if x == 0:
            a = abs(sy)
            b = abs(sy)
        elif y > 0:
            if x > 0 and y <= x:
                a = abs(x)
                b = 0
            elif x > 0 and y > x:
                a = abs(sy)
                b = abs(sy) - abs(x)
            elif x < 0 and y <= -x:
                b = abs(x)
                a = 0
            elif x < 0 and y > -x:
                b = abs(sy)
                a = abs(sy) - abs(x)
        
        elif y == 0 and x != 0:
            if x < 0:
                a = 0
                b = abs(sx)
            elif x > 0:
                a = abs(sx)
                b = 0
        elif y < 0:
            if x > 0 and y >= -x:
                a = abs(x)
                b = 0
            elif x > 0 and y < -x:
                a = abs(sy)
                b = abs(sy) - abs(x)
            elif x < 0 and y >= x:
                a = 0
                b = abs(x)
            elif x < 0 and y < x:
                a = abs(sy) - abs(x)
                b = abs(sy)
        #if j.get_name() == 'wide':
            #a = x
            #b = x
        else:
            a = 0
            b = 0
               

    ######################################
    ## PWM convertion for AnalogueWrite()#
    ######################################

        PWM = 255
        a = PWM*a
        a = round(a, 1)
        b = PWM*b
        b = round(b, 1)

    ###################################
    # Arduino Varibles Decleared Here!#
    ###################################

        motor_a = a
        motor_b = b

    ####################################
    # NEW: Single PWM Channel LOW fix! #
    ####################################
        if robot_detection == 'CMDoverwatch' or robot_detection == 'home':
            if y < 0:           
                y = 2                # Backwards
            else:               
                y = 1                # Forewards
            dir_y = y
        elif robot_detection == 'CMDrecon':
            if y < 0:           
                y = 2                # Backwards
                #motor_a = 255 - abs(motor_a)
                #motor_a = abs(motor_a)
                #motor_b = 255 - abs(motor_b)
                #motor_b = abs(motor_b)
            else:               
                y = 1                # Forewards
            dir_y = y
    ###############################
    #  NEW: Servo Control Script! #
    ###############################

    ##        servo_control = 45*abs(x)
    ##    
    ##        if x > 0:
    ##            servo = 90 + servo_control
    ##        elif x < 0:
    ##            servo = 90 - servo_control
    ##        else:
    ##            servo = 90
    ##        servo = round(servo, 0)
##        if z == 0:
##            servo = 90
##        elif z == 0.5:
##            servo = 98
##        elif z == -0.5:
##            servo = 82
##        elif z == 1:
##            servo = 105
##        elif z == -1:
##            servo = 75
        
    ##########################################
    # Sends data ONLY when data is different!#
    ##########################################

        if tcp_enabled == "y":
            if motor_a != motor_a_prev:
                sendcommand()
            elif motor_b != motor_b_prev:
                sendcommand()
            elif dir_y != dir_y_prev:
                sendcommand()
##            elif servo != servo_prev:
##                   sendcommand()


            motor_a_prev = motor_a
            motor_b_prev = motor_b
            dir_y_prev = dir_y
##            servo_prev = servo


    ####################################
    # Printing Output - Only used in   #
    # development of Joystick Control. #
    ####################################

        print (int(a),int(b), int(servo))
    
except KeyboardInterrupt:
    if tcp_enabled == "y":
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
    sys.exit("Closing Application...")

#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################

    
##################
#CUSTOM FUNCTIONS#  Currently unstable, to make usable in coming updates
##################


while i == "button":
    pygame.event.pump()
    if j.get_button(1):
        print "Left"
    if j.get_button(0):
        print "Kill"
    if j.get_button(2):
        print "Right"

###################################################

while i == "speed":
    print"currently in progress"
    x = 0.4
    y = 0.5
    f = 100
    sy = f*abs(y)
    print sy


###################################################


while i == "all":
    pygame.event.pump()
    y = j.get_axis(1)
    y = round(y,2)
    x = j.get_axis(0)
    x = round(x,2)
    z = j.get_axis(2)
    z = round(z,1)
    if j.get_button(0):
        b0 = " Kill"
    else:
        b0 = ""
    if j.get_button(1):
        b1 = " Left"
    else:
        b1 = ""
    if j.get_button(2):
        b2 = " Right"
    else:
        b2 = ""
    print(str(x) + "," + str(y) + "," + str(z) + b0 + b1 + b2)

'''CMD Official Comment ART

#####################################
###     #####    ##    #####      ###
##  ########   #    #   ####  ###  ##
##  ########  ###  ###  ####  #### ##
##  ########  ###  ###  ####  ###  ##
###     ####  ###  ###  ####      ###
#####################################
'''
endstatement = raw_input("You have reached the end of the script! (exit/ *) ")
if endstatement == "exit":
    sys.exit("End of script!")

```

### XAML ###
XAML runs all the graphics for this particular application and does nothing more.

```
<Window 
       xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
       xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" x:Name="form1" 
       Title="CMD Robot Control System - Beta Release 3" Height="319" Width="553" WindowStartupLocation="CenterScreen" ResizeMode="NoResize">
    <Grid Background="#FF92D5E4">
        <Grid.RowDefinitions>
            <RowDefinition Height="177*"/>
            <RowDefinition Height="11*"/>
            <RowDefinition Height="102*"/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="37*"/>
            <ColumnDefinition Width="237*"/>
            <ColumnDefinition Width="21*"/>
            <ColumnDefinition Width="12*"/>
            <ColumnDefinition Width="233*"/>
            <ColumnDefinition Width="7*"/>
        </Grid.ColumnDefinitions>
        
        <Rectangle Grid.Column="4" HorizontalAlignment="Left" Height="299" Margin="14,0,-9,-9" VerticalAlignment="Top" Width="235" Grid.RowSpan="3" Fill="#FFDBF4F9" Grid.ColumnSpan="2" Stroke="Black"/>
        <Rectangle Fill="#FFDBF4F9" HorizontalAlignment="Left" Height="97" Margin="15,87,0,0" Stroke="Black" VerticalAlignment="Top" Width="285" Grid.ColumnSpan="4" Grid.RowSpan="2" RadiusY="4" RadiusX="4"/>
        <Button x:Name="Start_Button" Content="Start" HorizontalAlignment="Left" Height="27" Margin="17,33,0,0" VerticalAlignment="Top" Width="64" Click="Start_Button_Click" Grid.Row="2" Grid.ColumnSpan="2" Foreground="White" Background="#FF7EBB13"/>
        <Button x:Name="Info_Button" Content="Info" HorizontalAlignment="Left" Height="27" Margin="53,33,0,0" VerticalAlignment="Top" Width="64" Click="Info_Button_Click" Grid.Row="2" Background="#FFFFF272" Grid.Column="1"/>
        <Button x:Name="Close_Button" Content="Close" HorizontalAlignment="Left" Height="27" Margin="199,33,0,0" VerticalAlignment="Top" Width="64" Click="Close_Button_Click" Grid.Row="2" Grid.ColumnSpan="3" Background="#FFE43F3F" Grid.Column="1"/>
        <RadioButton x:Name="CMDoverwatch_radiobutton" Content="CMDoverwatch" HorizontalAlignment="Left" Height="17" Margin="22,93,0,0" VerticalAlignment="Top" Width="107" Checked="CMDoverwatch_radiobutton_Checked" FontWeight="Bold" Grid.ColumnSpan="2"/>
        <RadioButton x:Name="CMDrecon_radiobutton" Content="CMDrecon" HorizontalAlignment="Left" Height="16" Margin="129,93,0,0" VerticalAlignment="Top" Width="103" Checked="CMDrecon_radiobutton_Checked" FontWeight="Bold" Cursor="" Grid.Column="1"/>
        <TextBlock x:Name="IPaddress_Textblock" HorizontalAlignment="Left" Height="25" Margin="6,122,0,0" TextWrapping="Wrap" VerticalAlignment="Top" Width="73" FontWeight="Bold" Grid.Column="1"><Run Text="IP Address:"/></TextBlock>
        <TextBlock x:Name="Port_Textblock" HorizontalAlignment="Left" Height="22" Margin="6,150,0,0" TextWrapping="Wrap" VerticalAlignment="Top" Width="77" FontWeight="Bold" Grid.Column="1"><Run Language="en-au" Text="Port:"/></TextBlock>
        <TextBox x:Name="Port_TextBox" HorizontalAlignment="Left" Height="22" Margin="129,150,0,0" TextWrapping="Wrap" Text="8999" VerticalAlignment="Top" Width="118" TextChanged="Port_TextBox_TextChanged" GotFocus ="Port_TextBox_GotFocus" BorderThickness="0.5" Grid.Column="1" Grid.ColumnSpan="2"/>
        <TextBox x:Name="IPaddress_TextBox" HorizontalAlignment="Left" Height="24" Margin="129,121,0,0" TextWrapping="Wrap" Text="10.0.0.1" VerticalAlignment="Top" Width="117" TextChanged="IPaddress_TextBox_TextChanged" GotFocus ="IPaddress_TextBox_GotFocus" BorderThickness="0.5" Grid.Column="1" Grid.ColumnSpan="2"/>
        <TextBlock HorizontalAlignment="Left" Height="23" Margin="22,88,0,-9" TextWrapping="Wrap" VerticalAlignment="Top" Width="278" Cursor="Help" FontSize="9" Grid.Row="2" Opacity="0.6" Grid.ColumnSpan="4"><Run Language="en-au" Text="Created by Tom Ingram and Cian Byrne ©"/><Run Text=" CMDenterprises"/><Span Language="en-au"><Run Text="™ 2013"/></Span><LineBreak/><Run Language="en-au"/><LineBreak/><Run Language="en-au"/></TextBlock>
        <TextBlock x:Name="TextBlock_TextBlock" HorizontalAlignment="Left" Height="19" Margin="17,63,0,0" TextWrapping="Wrap" Text="Select Robot" VerticalAlignment="Top" Width="85" FontWeight="Bold" TextDecorations="{x:Null}" Grid.ColumnSpan="2"/>
        <TextBlock x:Name="Custom1_textblock" HorizontalAlignment="Left" Height="22" Margin="92,42,0,0" TextWrapping="Wrap" VerticalAlignment="Top" Width="84" Foreground="Black" FontFamily="Arial Black" TextDecorations="{x:Null}" FontSize="16" Grid.Column="4"><Run Language="en-au" Text="Settings"/></TextBlock>
        <TextBlock TextWrapping="Wrap" Text="Current User is:" VerticalAlignment="Top" Height="21" Margin="0,37,108,0" FontFamily="Arial Black" Background="Black" Foreground="White" LineHeight="6" RenderTransformOrigin="0.5,0.5" Padding="16,3,0,0" Grid.ColumnSpan="2"/>
        <TextBox x:Name="User_TextBox_New" Height="21" Margin="129,37,219,0" TextWrapping="Wrap" Text="User" VerticalAlignment="Top" Cursor="Hand" FontFamily="Arial Black" BorderThickness="0" TextChanged="User_TextBox_New_TextChanged" Background="Black" Grid.ColumnSpan="4" Padding="0,3,0,0" Foreground="White" Focusable="False" IsHitTestVisible="False" AllowDrop="False" Grid.Column="1"/>
        <Rectangle Fill="#FF92D5E4" HorizontalAlignment="Left" Height="54" Stroke="Black" VerticalAlignment="Top" Width="565" Grid.ColumnSpan="6" Margin="-9,-17,-9,0"/>
        <TextBlock HorizontalAlignment="Left" Margin="116,10,0,0" TextWrapping="Wrap" VerticalAlignment="Top" Height="22" Width="264" FontFamily="Stencil" FontSize="18" Grid.ColumnSpan="4" Grid.Column="1"><Run Text="CMD Robot Control System"/><Run Language="en-au" Text=" Beta"/><Run Language="en-au" Text=" Be"/></TextBlock>
        <Button x:Name="btn_test" Content="Test" HorizontalAlignment="Left" Margin="127,33,0,0" Grid.Row="2" VerticalAlignment="Top" Width="64" Height="27" Click="btn_test_Click" Background="#FFF9B551" Grid.Column="1"/>
        <CheckBox x:Name="dev_CheckBox" Content="Developer Mode" HorizontalAlignment="Left" Height="22" Margin="38,171,0,0" VerticalAlignment="Top" Width="137" Checked="dev_CheckBox_Checked" Unchecked="dev_CheckBox_UnChecked" Grid.Column="4" Grid.RowSpan="3"/>
        <CheckBox x:Name="JoystickEnable_CheckBox" Content="Joystick Enabled" HorizontalAlignment="Left" Margin="38,87,0,0" VerticalAlignment="Top" Grid.Column="4" Checked="JoystickEnable_CheckBox_Checked"/>
        <CheckBox x:Name="DebugEnabled_CheckBox" Content="Debug Mode Enabled" Grid.Column="4" HorizontalAlignment="Left" Height="25" Margin="38,117,0,0" VerticalAlignment="Top" Width="149" Checked="DebugEnabled_CheckBox_Checked"/>
        <CheckBox x:Name="TCPEnabled_CheckBox" Content="TCP Client Enabled" Grid.Column="4" HorizontalAlignment="Left" Height="25" Margin="38,145,0,0" VerticalAlignment="Top" Width="162" Checked="TCPEnabled_CheckBox_Checked"/>
    </Grid>
</Window>

```

### details.txt ###
Some may be wondering why there is a file in the source called details.txt that has weird stuff in it like below.  This is how we got our information out of Ironpython and into the python client.  It is not a very nice way to do it because file permissions could cause the program to crash.  So anyway, we elimated this process in the vb.net port.  Here is the file content anyway.

NOTE: this information changes based on user configuration.

```
9999
localhost
CMDoverwatch
y
y
n
```

### Screen Designs for CMD-Robot Control System (RCS) Beta ###

![http://www.gdriveurl.com/?idl=913793320162&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=913793320162&out=1&nonsense=something_that_ends_with.png)
![http://www.gdriveurl.com/?idl=113793319949&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=113793319949&out=1&nonsense=something_that_ends_with.png)
![http://www.gdriveurl.com/?idl=413793320422&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=413793320422&out=1&nonsense=something_that_ends_with.png)
![http://www.gdriveurl.com/?idl=813793320622&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=813793320622&out=1&nonsense=something_that_ends_with.png)



## CMD3C for Windows ##
This piece of software was the last that we created and implemented a full VB.NET port of the program.  This was difficult because we had to learn about a new module called "Microsoft.DirectX.DirectInput" which allows one to use a joystick with Windows' accelerated graphics and input driver.  That way we did not need anything running in the background and could use a nice closed system for running everything.

It also gave us an opportunity to play around with embedded video feeds and so forth.  Most of the extra stuff does not work in this as it is still under-development pending release.

We also implemented new socket modules from the "System.Net.Sockets" module available in the .NET framework.

Here it goes.

### VB.NET - JoyTCP.vb (code) ###
Runs the Joystick and TCP Client after options have been decided.

```
Imports Microsoft.DirectX
Imports Microsoft.DirectX.DirectInput
Imports System.Net
Imports System.Net.Sockets

Public Class JoyTCP
    Property DefaultCharIsUnsigned As Boolean
    Dim Joystick As Device
    Dim ValueToSend As String
    Dim Paused As Boolean
    Dim _HOST As String = ""
    Dim _PORT As String = ""
    Dim _JoystickEn As String = ""
    Dim _DebugEn As String = ""
    Dim _TCPEn As String = ""
    Dim _CMDrobot As String = ""
    Dim oldValueToSend As String = ""
    Dim x As Integer = 0
    Dim y As Integer = 0
    Dim a As Integer = 0
    Dim b As Integer = 0

    Public Sub JoyTCP_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        GetVariablesFromStartForm()

        If _JoystickEn = "y" Then
            InitializeJoystick()
        End If
        txtbox_robot.Text = _CMDrobot
        If _TCPEn = "y" Then
            _ServerAddress = Nothing
            Dim remoteHost As IPHostEntry = Dns.GetHostEntry(StartForm.txtbox_IPaddr.Text)
            If remoteHost IsNot Nothing AndAlso remoteHost.AddressList.Length > 0 Then
                For Each deltaAddress As IPAddress In remoteHost.AddressList
                    If deltaAddress.AddressFamily = AddressFamily.InterNetwork Then
                        _ServerAddress = deltaAddress
                        Exit For
                    End If
                Next
            End If

            If _ServerAddress Is Nothing Then
                MessageBox.Show("Cannot resolove server address.", "Invalid Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
                StartForm.txtbox_Port.SelectAll()
            End If
            Connect()
        End If
        If _TCPEn = "n" Then
            btn_connect.Enabled = False
            btn_pause.Enabled = False
            btn_disconnect.Enabled = False
        End If
    End Sub
    Private Sub JoyPoll()
        Try
            Joystick.Poll()
            Dim state As JoystickState = Joystick.CurrentJoystickState
            Dim x As Integer
            Dim y As Integer
            Dim a As Integer
            Dim b As Integer
            Dim Direction As Integer
            Dim Button0 As Integer
            Dim Button1 As Integer
            Dim Button2 As Integer
            Dim Button3 As Integer
            Dim motor_a As Integer
            Dim motor_b As Integer
            Dim dir As Integer

            txtbox_Xcord.Text = state.X
            txtbox_Ycord.Text = state.Y
            txtbox_Zcord.Text = state.Z
            txtbox_RZcord.Text = state.Rz
            Button0 = state.GetButtons(0)
            Button1 = state.GetButtons(1)
            Button2 = state.GetButtons(2)
            Button3 = state.GetButtons(3)
            txtbox_Button0.Text = Button0
            txtbox_Button1.Text = Button1
            txtbox_Button2.Text = Button2
            txtbox_Button3.Text = Button3
            x = state.X
            y = state.Y

            If y < 0 Then
                y = Math.Abs(y)
                Direction = 1
            ElseIf y > 0 Then
                y = y * -1
                Direction = 2
            End If

            If Button1 = 0 And Button2 = 0 Then
                If x = 0 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                ElseIf y > 0 Then
                    If x > 0 And y <= x Then
                        a = Math.Abs(x)
                        b = 0
                    ElseIf x > 0 And y > x Then
                        a = Math.Abs(y)
                        b = Math.Abs(y) - Math.Abs(x)
                    ElseIf x < 0 And y <= -x Then
                        b = Math.Abs(x)
                        a = 0
                    ElseIf x < 0 And y > -x Then
                        b = Math.Abs(y)
                        a = Math.Abs(y) - Math.Abs(x)
                    End If
                ElseIf y = 0 And x <> 0 Then
                    If x < 0 Then
                        a = 0
                        b = Math.Abs(x)
                    ElseIf x > 0 Then
                        a = Math.Abs(x)
                        b = 0
                    End If
                ElseIf y < 0 Then
                    If x > 0 And y >= -x Then
                        a = Math.Abs(x)
                        b = 0
                    ElseIf x > 0 And y < -x Then
                        a = Math.Abs(y)
                        b = Math.Abs(y) - Math.Abs(x)
                    ElseIf x < 0 And y >= x Then
                        a = 0
                        b = Math.Abs(x)
                    ElseIf x < 0 And y < x Then
                        a = Math.Abs(y) - Math.Abs(x)
                        b = Math.Abs(y)
                    Else
                        a = 0
                        b = 0
                    End If
                End If
            ElseIf Button1 = 128 Or Button2 = 128 Then
                If Button1 = 128 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                    Direction = 3
                ElseIf Button2 = 128 Then
                    a = Math.Abs(y)
                    b = Math.Abs(y)
                    Direction = 4
                End If
            End If

            lbl_value_a.Text = Math.Round((a / 255) * 100) 'CHANGED so that is displays a percentage, not sure if working :D
            lbl_value_b.Text = Math.Round((b / 255) * 100)
            a = Math.Round(a, 1)
            b = Math.Round(b, 1)
            motor_a = Int(a)
            motor_b = Int(b)
            dir = Int(Direction)
            ValueToSend = (Chr(motor_a) & Chr(motor_b) & Chr(dir))
            If ValueToSend <> oldValueToSend Then
                If Paused = False Then
                    SendData()
                    oldValueToSend = ValueToSend
                End If
            End If

            'If Paused = False Then
            '    SendData()
            'End If
        Catch ex As Exception
        End Try
    End Sub

    Private Sub InitializeJoystick()
        Dim oInst As DeviceInstance
        Dim oDOInst As DeviceObjectInstance

        For Each oInst In Manager.GetDevices(DeviceClass.GameControl, EnumDevicesFlags.AttachedOnly)
            Joystick = New DirectInput.Device(oInst.InstanceGuid)
            Exit For
        Next

        If Not (Joystick Is Nothing) Then
            Joystick.SetDataFormat(DeviceDataFormat.Joystick)
            Joystick.SetCooperativeLevel(Me, CooperativeLevelFlags.NonExclusive Or DirectInput.CooperativeLevelFlags.Background)
            For Each oDOInst In Joystick.Objects
                If 0 <> (oDOInst.ObjectId And CInt(DeviceObjectTypeFlags.Axis)) Then
                    Joystick.Properties.SetRange(ParameterHow.ById, oDOInst.ObjectId, New InputRange(-255, +255))
                End If
            Next
        End If

        Try
            Joystick.Acquire()
        Catch ex As Exception
            MessageBox.Show(ex.Message, "Couldn't detect joystick!", MessageBoxButtons.OK, MessageBoxIcon.Error)
        End Try

        Timer1.Start()
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        If _JoystickEn = "y" Then
            JoyPoll()
        End If
    End Sub

    Private Sub GetVariablesFromStartForm()
        _HOST = StartForm.txtbox_IPaddr.Text
        _PORT = StartForm.txtbox_Port.Text
        If StartForm.rabtn_CMDoverwatch.Checked = True Then
            _CMDrobot = "CMDoverwatch"
        ElseIf StartForm.rabtn_CMDrecon.Checked = True Then
            _CMDrobot = "CMDrecon"
        ElseIf StartForm.RadioButton1.Checked = True Then
            _CMDrobot = "CMDdebug"
        End If
        If StartForm.CheckBox_JoystickEn.Checked = True Then
            _JoystickEn = "y"
        Else
            _JoystickEn = "n"
        End If
        If StartForm.CheckBox_DebugmodeEn.Checked = True Then
            _DebugEn = "y"
        Else
            _DebugEn = "n"
        End If
        If StartForm.CheckBox_TCPclientEn.Checked = True Then
            _TCPEn = "y"
        Else
            _TCPEn = "n"
        End If
    End Sub

    Private _Connection As ConnectionInfo
    Private _ServerAddress As IPAddress
    Public Sub Connect()
        If _ServerAddress IsNot Nothing Then
            Try
                '_Connection = New ConnectionInfo(_ServerAddress, CInt(txtbox_Port.Text), AddressOf InvokeAppendOutput)
                _Connection = New ConnectionInfo(_ServerAddress, CInt(StartForm.txtbox_Port.Text), AddressOf InvokeAppendOutput)
                '_Connection = New ConnectionInfo(_ServerAddress, CInt(StartForm.txtbox_Port.Text))
                _Connection.AwaitData()
            Catch ex As Exception
                MessageBox.Show(ex.Message, "Error Connecting to Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
            End Try
        Else
            MessageBox.Show("Invalid server name or address. Try inputting it again!", "Cannot Connect to Server", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End If
    End Sub

    'The InvokeAppendOutput method could easily be replaced with a lambda method passed
    'to the ConnectionInfo contstructor in the ConnectButton_CheckChanged event handler
    Private Sub InvokeAppendOutput(message As String)
        Dim doAppendOutput As New Action(Of String)(AddressOf AppendOutput)
        Me.Invoke(doAppendOutput, message)
    End Sub
    'Private Sub AppendOutput(message As String)
    '    If StartForm.RichTextBox1.TextLength > 0 Then
    '        StartForm.RichTextBox1.AppendText(ControlChars.NewLine)
    '    End If
    '    StartForm.RichTextBox1.AppendText(message)
    '    StartForm.RichTextBox1.ScrollToCaret()
    'End Sub
    Public Sub SendData()
        If _Connection IsNot Nothing AndAlso _Connection.Client.Connected AndAlso _Connection.Stream IsNot Nothing Then
            Dim buffer() As Byte = System.Text.Encoding.Default.GetBytes(ValueToSend)
            _Connection.Stream.Write(buffer, 0, buffer.Length)
        End If
    End Sub
    Private Sub btn_disconnect_Click(sender As Object, e As EventArgs)
        _Connection.Close()
    End Sub

    '   Private Sub btn_pause_Click(sender As Object, e As EventArgs)
    '    If btn_pause.Text = "Pause" Then
    '        Paused = True
    '        btn_pause.Text = "Play"
    '        MessageBox.Show("Box shown!!  Play button pressed")
    '    ElseIf btn_pause.Text = "Play" Then
    '        Paused = False
    '        btn_pause.Text = "Pause"
    '        MessageBox.Show("Box shown!!  Pause button pressed")
    '    End If
    'End Sub

    'Private Sub btn_Forcetest_Click(sender As Object, e As EventArgs)
    '    lbl_value_a.Text = "75"
    '    lbl_value_b.Text = "100"
    '    MessageBox.Show("btn_Forcetest_Clicked")
    'End Sub

    Private Sub btn_close_Click(sender As Object, e As EventArgs) Handles btn_close.Click
        StartForm.Close()
        Me.Close()
    End Sub

    

    Private Sub btn_Forcetest_Click_1(sender As Object, e As EventArgs) Handles btn_Forcetest.Click
        lbl_value_a.Text = "75"
        lbl_value_b.Text = "100"
    End Sub

    Private Sub btn_connect_Click_1(sender As Object, e As EventArgs) Handles btn_connect.Click
        Connect()
    End Sub

    Private Sub btn_pause_Click_1(sender As Object, e As EventArgs) Handles btn_pause.Click
        If btn_pause.Text = "Pause" Then
            Paused = True
            btn_pause.Text = "Play"
            'MessageBox.Show("Box shown!!  Play button pressed")
        ElseIf btn_pause.Text = "Play" Then
            Paused = False
            btn_pause.Text = "Pause"
            'MessageBox.Show("Box shown!!  Pause button pressed")
        End If
    End Sub

    Private Sub btn_disconnect_Click_1(sender As Object, e As EventArgs) Handles btn_disconnect.Click
        _Connection.Close()
    End Sub

    Private Sub AppendOutput()
        Throw New NotImplementedException
    End Sub


End Class

'Encapuslates the client connection and provides a state object for async read operations
Public Class ConnectionInfo
    Private _AppendMethod As Action(Of String)
    Public ReadOnly Property AppendMethod As Action(Of String)
        Get
            Return _AppendMethod
        End Get
    End Property

    Private _Client As TcpClient
    Public ReadOnly Property Client As TcpClient
        Get
            Return _Client
        End Get
    End Property

    Private _Stream As NetworkStream
    Public ReadOnly Property Stream As NetworkStream
        Get
            Return _Stream
        End Get
    End Property

    Private _LastReadLength As Integer
    Public ReadOnly Property LastReadLength As Integer
        Get
            Return _LastReadLength
        End Get
    End Property

    Private _Buffer(63) As Byte

    Public Sub New(address As IPAddress, port As Integer, append As Action(Of String))
        _AppendMethod = append
        _Client = New TcpClient
        _Client.Connect(address, port)
        _Stream = _Client.GetStream
    End Sub

    Public Sub AwaitData()
        _Stream.BeginRead(_Buffer, 0, _Buffer.Length, AddressOf DoReadData, Me)
    End Sub

    Public Sub Close()
        If _Client IsNot Nothing Then _Client.Close()
        _Client = Nothing
        _Stream = Nothing
    End Sub

    Private Sub DoReadData(result As IAsyncResult)
        Dim info As ConnectionInfo = CType(result.AsyncState, ConnectionInfo)
        Try
            If info._Stream IsNot Nothing AndAlso info._Stream.CanRead Then
                info._LastReadLength = info._Stream.EndRead(result)
                If info._LastReadLength > 0 Then
                    Dim message As String = System.Text.Encoding.ASCII.GetString(info._Buffer)
                    info._AppendMethod(message)
                End If
                info.AwaitData()
            End If
        Catch ex As Exception
            info._LastReadLength = -1
            info._AppendMethod(ex.Message)
        End Try
    End Sub
End Class

```

### Design for JoyTCP.py ###

![http://www.gdriveurl.com/?idl=413793313318&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=413793313318&out=1&nonsense=something_that_ends_with.png)
![http://www.gdriveurl.com/?idl=113793315367&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=113793315367&out=1&nonsense=something_that_ends_with.png)


### VB.NET - Form1.vb (code) ###
This is the first load screen where the user gets to choose what they want to control and what other settings they want.

```
Imports System.Net
Imports System.Net.Sockets

Public Class StartForm
    Dim CMDrobot As String = ""
    Dim IPaddr As String = ""
    Dim Port As String = ""
    Dim DebugEn As String = ""
    Dim JoystickEn As String = ""
    Dim TCPEn As String = ""

    Private Sub btn_start_Click(sender As Object, e As EventArgs) Handles btn_start.Click
        IPaddr = txtbox_IPaddr.Text
        Port = txtbox_Port.Text
        CMDrobot = CMDrobot
        If CheckBox_JoystickEn.Checked = True Then
            JoystickEn = "y"
        Else
            JoystickEn = "n"
        End If
        If CheckBox_DebugmodeEn.Checked = True Then
            DebugEn = "y"
        Else
            DebugEn = "n"
        End If
        If CheckBox_TCPclientEn.Checked = True Then
            TCPEn = "y"
        Else
            TCPEn = "n"
        End If
        JoyTCP.Show()
    End Sub

    Private Sub btn_close_Click(sender As Object, e As EventArgs) Handles btn_close.Click
        Me.Close()
    End Sub

    Private Sub CheckBox_DevEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_DevEn.CheckedChanged
        If CheckBox_DevEn.Checked = True Then
            btn_testmode.Enabled = True
        Else
            btn_testmode.Enabled = False
        End If
    End Sub

    Private Sub btn_testmode_Click(sender As Object, e As EventArgs) Handles btn_testmode.Click
        MessageBox.Show("Welcome to the Dev console, in future this will launch the Black Frost Console!", "Dev Console Alert")
        'Joystick_TCP.Show()
    End Sub

    Private Sub rabtn_CMDoverwatch_CheckedChanged(sender As Object, e As EventArgs) Handles rabtn_CMDoverwatch.CheckedChanged
        CMDrobot = "CMDoverwatch"
        txtbox_IPaddr.Text = "10.0.0.1"
        txtbox_Port.Text = "8999"
    End Sub

    Private Sub rabtn_CMDrecon_CheckedChanged(sender As Object, e As EventArgs) Handles rabtn_CMDrecon.CheckedChanged
        CMDrobot = "CMDrecon"
        txtbox_IPaddr.Text = "10.0.0.10"
        txtbox_Port.Text = "9999"
    End Sub

    Private Sub CheckBox_JoystickEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_JoystickEn.CheckedChanged
        If CheckBox_JoystickEn.Checked = True Then
            CheckBox_DebugmodeEn.Checked = False
        End If
    End Sub

    Private Sub CheckBox_DebugmodeEn_CheckedChanged(sender As Object, e As EventArgs) Handles CheckBox_DebugmodeEn.CheckedChanged
        If CheckBox_DebugmodeEn.Checked = True Then
            CheckBox_JoystickEn.Checked = False
        End If
    End Sub


    Private Sub StartForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub RadioButton1_CheckedChanged(sender As Object, e As EventArgs) Handles RadioButton1.CheckedChanged
        txtbox_IPaddr.Text = "localhost"
        txtbox_Port.Text = "9999"
        CMDrobot = "CMDdebug"
    End Sub

End Class

```

### Design for Form1.vb ###

![http://www.gdriveurl.com/?idl=813793316232&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=813793316232&out=1&nonsense=something_that_ends_with.png)


### VideoBoxForm ###
As this code is in Pre-Alpha stages, we shall not give an explanation.

WARNING: May not work correctly!! or at all!!!

```
Public Class VideoBoxForm
    Dim VideoStream As String = ""
    Private Sub VideoBoxForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' txtbox_VideoServer.Text = "192.168.12.43"
        'VideoStream = txtbox_VideoServer.Text
        txt_streambox.Text = "http://cmdlab.zapto.org:81/videostream.cgi?&user=admin&pwd="
    End Sub

    Private Sub Button1_Click_1(sender As Object, e As EventArgs)
        'A nice test video for you www.youtube.com/watch?v=dd3j0Qpq0tI
        streambox.stop()
        streambox.playlistClear()
        Dim address As String
        address = txt_streambox.Text
        streambox.addTarget(address, Nothing, AXVLC.VLCPlaylistMode.VLCPlayListReplaceAndGo, 0)
        streambox.play()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs)
        streambox.stop()
        streambox.playlistClear()
    End Sub

    Private Sub txt_streambox_DoubleClick(sender As Object, e As EventArgs)
        txt_streambox.SelectAll()
    End Sub

End Class

```

### Design for VideoBoxForm.vb ###

![http://www.gdriveurl.com/?idl=413793317415&out=1&nonsense=something_that_ends_with.png](http://www.gdriveurl.com/?idl=413793317415&out=1&nonsense=something_that_ends_with.png)


# Conclusion #

All of the above source is not for public use as it could be dangerous to the uses of the it.  Also not that direct code and paste of the code would be rude.

In Conclusion, All of the above code has taken ages to code and we would like to thank anyone who has helped along the way or the people who wrote the MSDN, Python Doc, and all the other forums that we have researched to make all of the above code.  The Development community is great!