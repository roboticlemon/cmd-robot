import socket
import sys

HOST, PORT = "192.168.12.46", 8899
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

try:
    while True:
        i = input('Enter Number between 0 - 180: ')
        Byte1 = chr(int(i))
        sock.send(Byte1)
except KeyboardInterrupt:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.exit("Closing Application...")
