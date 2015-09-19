print "Welcome to TCP debug! Version 1.4.2"
from time import sleep
import sys
import os
import socket
'''
TCP Server gets hostname from local machine and uses the hostname to
get the IP address of the Machine.

This is so that it does not matter what machine you are running the script
on, which means that you don't need to change anything. :D

Cian Byrne
'''
#sleep(2.5)
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
            byte4 = chr(int(90)) #servo
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
        #hostname = socket.gethostname()
        #host = str(socket.gethostbyname_ex(hostname)[2]).strip("['']")
        #HOST = str(host)
	#HOST = "192.168.12.37"     # For Debugging
        HOST = "10.0.0.1"
        PORT = 8999                 # Reserve a port for your service.


    ######################################
    # Setup Serial interface if enabled. #
    ######################################

        if enableserial == 1:
            import serial
            #DEVICE = '/dev/ttyACM0' # the arduino serial interface (use dmesg when connecting)
            #DEVICE = 'COM8'
            DEVICE = '/dev/ttyAMA0'  #Raspberry Pi Serial Port RX/TX
            BAUD = 9600
            ser = serial.Serial(DEVICE, BAUD)
            
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
            
