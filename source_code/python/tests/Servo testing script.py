# Testing Servo for Arduino Sketch
# Written by Cian Byrne
try:
    import serial
    import sys
    DEVICE = 'COM12'
    BAUD = 9600
    ser = serial.Serial(DEVICE, BAUD)

    while True:
        Byte = input("Enter a value between 0 - 180: ")
        #Byte = chr(int(Byte))
        ser.write(Byte)
    
except KeyboardInterrupt:
   print "closing shell..."
   ser.close()
   sys.exit("Closing Application...")
