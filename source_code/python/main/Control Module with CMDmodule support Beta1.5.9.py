print "*************************"        ###########################################
print "*Module version Beta 1.5*"        #     #####     ##    ##      #####       #
print "*Standby for imports....*"        #   ####      #    ##    #     ####  ###  #
print "*************************"        #   ##       ###  ####  ###    ####  #### #
print "                         "        #   ###      ###  ####  ###    ####  ###  #
import pygame                            #     #####  ###  ####  ###    ####       #
import socket                            ###########################################
import sys                               #Revision number: 2                       # 
import os                                ###########################################
from time import gmtime, strftime, sleep
from pygame.locals import *
from CMDmodule import *


##################
#Asset Detection!#
##################

if os.path.exists("C:\Users\Tom"):
    commander_name = "Ingram"
elif os.path.exists("C:\Users\Cian"):
    commander_name = "Byrne"
else:
    commander_name = ""


time = strftime("%H:%M:%S")
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


print ("Welcome back Commander " + commander_name)
print ("You are running on " + os_type + " " + os_name + " with kernel version " + kernel_version)
print " "
print ("The current time is " + time)
print " "


##########################################
# Manual functionality specification     #
# Ingram & Byrne's idea                  #
##########################################

try:
    question_one = raw_input("Would you like to use Default Settings? (y/n): ")

    if question_one == "y":
        question_two = "y"
        question_three = "y"
        network_value = "y"
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
            print "[ SUCCESS ] Joystick Detected! [ SUCCESS ] "    
            print " "
        j = pygame.joystick.Joystick(0)
        j.init()
         
        print 'Initialized Joystick : %s' % j.get_name()

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

    if question_two == "y":
        if network_value == "n":
            network_one = raw_input("Would you like to use a pre-set IP address? (y/n): ")
            while network_one != "y" and network_one != "n":
                print "Please enter a valid value"
                network_one = raw_input("Would you like to use a pre-set IP address? (y/n): ")
                if network_one == "y" or network_one == "n":
                     break
            if network_one == "y":
                network_two = raw_input("Which pre-set IP do you want to use? ('adhoc'/'local'): ")
                while network_two != "adhoc" and network_two != "local":
                    print "Please enter a valid value"
                    network_two = raw_input("Which pre-set IP do you want to use? ('adhoc'/'local'): ")
                    if network_two == "adhoc" or network_two == "local":
                        break
                if network_two == "adhoc":
                    HOST, PORT = "192.168.12.1", 9999
                elif network_two == "local":
                    HOST, PORT = 'localhost', 9999
            elif network_one == "n":
                HOST = raw_input("Enter the Desired IP Address. (FORMAT: e.g. 192.168.12.1): ")
                PORT = raw_input("Enter the Desired Port number. (FORMAT: e.g. 9999): ")
        elif network_value == "y":
            HOST, PORT = "192.168.12.1", 9999


        print "                                                                  "
        print "****************************************************************************"
        print "*  [ ALERT ]  Stand by for TCP connection on " + str(HOST) + ":" + str(PORT)+" [ ALERT ]  *"
        print "****************************************************************************"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((HOST, PORT)) #'''Added in a try command for unsucessful TCP connection'''
            print " "                                                                  
            print " "
            print " "
            print "   [ ALERT ]   Connected to " + str(HOST) + ":" + str(PORT)+" [ ALERT ]   "
            print " "
            print " "
        except:
            print " "
            print "Unable to connect to " + HOST +", please check your connection!"
            print " "


    else:
        print "No TCP Client this sesson!"
except KeyboardInterrupt:
        if question_two == "y":
            sock.close()
        sys.exit("Closing Application...")


#########################################
# The mode that you want to enter which #
#  can be one of the following:         #
#########################################

try:
    if question_one != "y":
        if str(question_three) == "y":
            i = raw_input("What do you want to detect? (button/pos/all): ")
        elif str(question_three) == "n":
            debug_value = raw_input("Do you want to enter debug mode? (y/n): ")
        else:
            print "Enter a correct value next time!"
            sys.exit("Value Error!")
except KeyboardInterrupt:
        if question_two == "y":
            sock.close()
        sys.exit("Closing Application...")


######################################
#                                    #
#       D E B U G   M O D E          #
#                                    #
#      Advanced out of ALPHA         #
######################################
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
                    elif (event.key == K_s):
                        print "Moving Backwards!"
                        dir_y = 2
                        motor_a = 1
                        motor_b = 1                    
                    elif (event.key == K_d):
                        print "Moving Right!"
                        dir_y = 1
                        motor_b = 0
                        motor_a = 255
                    elif (event.key == K_w):
                        print "Moving Forwards!"
                        dir_y = 1
                        motor_a = 255
                        motor_b = 255
                    elif (event.key == K_ESCAPE):
                        done = True
                    else:
                        motor_a = 0
                        motor_b = 0                
                    if question_two == "y":
                        sendcommand(motor_a,motor_b,dir_y)
                    print (motor_a,motor_b)
except KeyboardInterrupt:
        if question_two == "y":
            sock.close()
        sys.exit("Closing Application...")

try:    
    while debug_value == "y":
        motor_a = input("LEFT MOTOR: Enter value between -255 and 255: ")
        motor_b = input("RIGHT MOTOR: Enter value between -255 and 255: ")
        if motor_a < 0 and motor_a > -256 or motor_b < 0 and motor_b > -256:
            dir_y = 2
            motor_a = 255 - abs(motor_a)
            motor_a = abs(motor_a)
            motor_b = 255 - abs(motor_b)
            motor_b = abs(motor_b)
            print "Going Backwards!"
            if question_two == "y":
                sendcommand(motor_a,motor_b,dir_y)
                print "Sent to server!"
        elif motor_a >= 0 and motor_a < 256 or motor_b >= 0 and motor_b < 256:               
            dir_y = 1
            motor_a = abs(motor_a)
            motor_b = abs(motor_b)
            print "Going Forwards!"
            if question_two == "y":
                sendcommand(motor_a,motor_b,dir_y)
                print "Sent to server!" 

        else:
            print "Number not in range, value not sent to server"
            print "Not sent to TCP Server!"
        print (motor_a, motor_b)
except KeyboardInterrupt:
        if question_two == "y":
            sock.close()
        sys.exit("Closing Application...")





###########################################################

try:
    while i == "pos":
        pygame.event.pump()
        y = j.get_axis(1)
        x = j.get_axis(0)   
        z = j.get_axis(2)   
        z = round(z,1)
        #print(x,y,z)
       
        invert_y_axis()
            
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
                   
                   

    ######################################
    ## PWM convertion for AnalogueWrite()#
    ######################################

        pwm_formula()

    ###################################
    # Arduino Varibles Decleared Here!#
    ###################################

        

    ####################################
    # NEW: Single PWM Channel LOW fix! #
    ####################################

        ardruino_direction_sPWM()


    ##########################################
    # Sends data ONLY when data is different!#
    ##########################################
        if question_two == "y":
            send_when_different()
    

####################################
# Printing Output - Only used in   #
# development of Joystick Control. #
####################################

        print (int(a),int(b))
        
except KeyboardInterrupt:
        if question_two == "y":
            sock.close()
        sys.exit("Closing Application...")

#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################

    
##################
#CUSTOM FUNCTIONS#  Currently unstable, to make usable in next update
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
