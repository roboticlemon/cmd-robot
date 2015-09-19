from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime            
import socket
import sys
import RPi.GPIO as gpio


#######################
# LCD interface setup!#
#######################

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
lcd = Adafruit_CharLCD()
lcd.begin(16,1)

#########################
# TCP Server Interface! #
#########################

s = socket.socket()         
host = '192.168.12.37'
port = 8888

####################
# Set-up Variables!#
####################

a = 0
b = 0
motor_a = 0
motor_b = 0


try: 
        print 'Server started!'
        print 'Waiting for clients...'
         
        s.bind((host, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr

        while True:
                data = c.recv(1024) #First lot of data
                data2 = c.recv(1024) #Second lot of data        
                #print ("motor1 = " +data + " motor 2 = " + data2 + "   $CMDcoders$")
                lcd.clear()
                ipaddr = run_cmd(cmd)
                lcd.message('A = ' +data + ' | B = ' +data2 + '/n')
                lcd.message('IP %s' % ( ipaddr ) )

except KeyboardInterrupt:
   print "Closing shell..."
   g.cleanup()
   s.close()
   sys.exit("Closing Application...")
   
