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

##configfile = open('details.txt', 'r')
##PORTA = configfile.readline().strip('\n')
##HOSTA = configfile.readline().strip('\n')
##robot_detection = configfile.readline().strip('\n')
##
##tcp_enabled = configfile.readline().strip('\n')
##joy_enabled = configfile.readline().strip('\n')
##debug_enabled = configfile.readline().strip('\n')

HOSTA = "10.0.0.1"
PORTA = 8999
robot_detection = "CMDoverwatch"
tcp_enabled = "y"
joy_enabled = "y"
debug_enabled = "n"



##print 'PORT: ' +PORTA
##print 'HOST: '+HOSTA
##print 'Robot: '+robot_detection
##print 'Joystick enabled: '+joy_enabled
##print 'Debug enabled: '+debug_enabled
##print 'TCP enabled: '+tcp_enabled
##sleep(3)

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
    init = 0
    while joy_enabled == "y":
        if tcp_enabled == "y":
            sockname = str(sockname)
        else:
            sockname = "nothing"
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
            sleep (3)

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
