# 1st Development Version of Joystick controller
# @wallarug
# @Ingramator

import pygame
import socket
import sys
import os
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
 
print 'Initialized Joystick : %s' % j.get_name()
username = os.name
if username == "nt":
    username = "Windows"
print "Welcome commander, you are using " + username
i = raw_input("What do you want to detect?")
while i == "button":
    pygame.event.pump()
    #print j.get_axis(1)
    if j.get_button(1):
        print "Left"
    if j.get_button(0):
        print "Kill"
    if j.get_button(2):
        print "Right"
while i == "pos":
    pygame.event.pump()
    y = j.get_axis(1)   ######################################
    y = round(y,2)      # Increase to (x, 12) when using PWM!#
    x = j.get_axis(0)   #  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   #
    x = round(x,2)      # Increase to (y, 12) when using PWM!#
    z = j.get_axis(2)   ######################################
    z = round(z,1)
    #print(x,y,z)
   
    if y < 0:          ############################
        y = abs(y)     #New Y-axes inversion code!#
    elif y > 0:        ############################
        y = y*-1

#############################################
# Formulas for working out the speed of the #
# motor in certain areas of the Joystick!   #
#############################################

    f = 100
    sy = f*(y)
    sx = f*(x)
    #PWM = 255

#############################################
## Whenever the ROBOT is moving and the     #
##  Co-ordinates are not (0,0)              #
#############################################

                                
    if x != 0 and y != 0:       
        sy = abs(sy)                    #######
        if y > abs(x) and y > 0:        # Top!#
                                        ############
            if -1 < x < 0:              # Top Left!#
                                        ############################################
                c = f*abs(x)            # Convert to percentage and positive value!#
                a = (sy) - (c)          ############################################
                b = (sy)
                                        #############
            elif 0 < x < 1:             # Top Right!#
                                        ############################################
                d = f*abs(x)            # Convert to percentage and positive value!#
                b = (sy) - (d)          ############################################
                a = (sy)
            else:
                a = abs(x)
                b = abs(x)

                                        ##########
        elif y < -abs(x) and y < 0:     # Bottom!#
                                        ###############
            if -1 < x < 0:              # Bottom Left!#
                                        ############################################
                c = f*abs(x)            # Convert to percentage and positive value!#
                a = (sy) - (c)          ############################################
                b = (sy)
                                        ################
            elif 0 < x < 1:             # Bottom Right!#
                                        ############################################
                d = f*abs(x)            # Convert to percentage and positive value!#
                b = (sy) - (d)          ############################################
                a = (sy)
            else:                       ############################################
                a = abs(sy)             # So that values "a" and "b" are regonised #
                b = abs(sy)             #  by python reader (I had problems)!      #
                                        ############################################

#######################################################################################
                                            
#################################
# Special formula for when you  #
#   leave the "allowed" area    #
#################################

        elif y < abs(x) and y > -abs(x):  
            if x < 0:
                b = abs(x)*f
                a = 0
            elif x > 0:
                a = abs(x)*f
                b = 0
            else:
                a = 0
                b = 0

######################################################################################

##################################
# Special Formula for all values #
#  on the x-axis for immediate   #
#    turning.                    #
##################################

    elif y == 0:
        if x < 0:
            a = 0
            b = abs(sx)
        elif x > 0:
            a = abs(sx)
            b = 0
        else:
            a = 0
            b = 0

#####################################################################################

#######################################
#  Anything else that is not defined  #
#   (Only when x and y = 0)           #
#######################################

    else:
        a = abs(sy)
        b = abs(sy)

        
####################################################################################               

######################################
### PWM convetion for AnalogueWrite()#
######################################
##    a = PWM*a
##    a = round(a,0)
##    a = int(a)
##    b = PWM*b
##    b = round(b,0)
##    b = int(b)


####################################################################################

####################################
# Printing Output - Only used in   #
# development of Joystick Control. #
####################################

    #print (a,b)

########################
# TCP client is below. #
########################

    data = (a,b)
    #data = raw_input("Enter your message to send to the server!:  ")
    HOST2, PORT2 = "10.88.112.174", 9998 # Change to server when necessary
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST2, PORT2))
    sock.sendall(str(data) + "\n")
    print "Sent:     {}".format(data)





#####################################################
##@@@@@@@@@@@@@@@@@@@@@@ END @@@@@@@@@@@@@@@@@@@@@ ##
#####################################################

    

while i == "speed":
    print"currently in progress"
    x = 0.4
    y = 0.5
    f = 100
    sy = f*abs(y)
    print sy
########
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
