from time import sleep
import sys
import socket
while True:
    s = socket.socket()         # Create a socket object
    host = 'localhost'          # Get local machine name
    port = 9998                 # Reserve a port for your service.


##    import serial
##    DEVICE = '/dev/ttyACM0' # the arduino serial interface (use dmesg when connecting)
##    ##DEVICE = 'COM12'
##    BAUD = 9600
##    ser = serial.Serial(DEVICE, BAUD)
    try: 
        print "Server started on", str(host) + ":" + str(port)
        print 'Waiting for clients...'
     
        s.bind((host, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr[0]
        while True:
            msg = c.recv(3) # get 3 bytes from the TCP connection
##            ser.write(msg)  # write the 3 bytes to the serial interface
            #print msg
            if msg == "":
                c.shutdown(socket.SHUT_RDWR)
                c.close()
                print "Lost connection with"+ str(addr) +"! Restarting server..."
                sleep(2)
                break
    except KeyboardInterrupt:
        print "[ALERT]  Closing shell...  [ALERT]"
        c.shutdown(socket.SHUT_RDWR)
        c.close()
##        ser.close()
        sys.exit("Application forcibly halted!")
