#exec(open("D:/Coding/python/CSC138/socket_programming4/example_code.py").read())
import socket
from socket import AF_INET, SOCK_DGRAM

import time

print("Running")

server = "127.0.0.1"

clientSocket = socket.socket(AF_INET,SOCK_DGRAM)

clientSocket.settimeout(1)

sequence_number = 1

while sequence_number<=10:

    message = "Ping".encode()

    start=time.time()

    clientSocket.sendto(message,(server, 8000))

    try:

        message, address = clientSocket.recvfrom(1024)

        timeElapsed = (time.time()-start) * 1000

        if timeElapsed:

            print("Reply from {}: time= {}ms seqnum= {}".format(address[0], str(timeElapsed), sequence_number))

    except socket.timeout:

        sequence_number+=1

    if sequence_number > 10:

        clientSocket.close()
