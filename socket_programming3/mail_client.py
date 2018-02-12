#!/usr/bin/env python3
#Socket programming 3

from socket import *
import ssl
import base64

def main():

    mailServer = 'smtp.gmail.com'
    mailPort = 587
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailServer, mailPort))

    data = clientSocket.recv(1024)
    print(data)
    if data[:3].decode('utf-8') != '220':
        print('220 reply not received from server.')

    clientSocket.send(b'HELO gmail.com\r\n')
    data2 = clientSocket.recv(1024)
    print(data2)
    if data2[:3].decode('utf-8') != '250':
        print('250 reply not received from server.')

    #starts data transfer
    clientSocket.send(b'starttls\r\n')
    print(clientSocket.recv(1024))

    #request for login
    secureConnect = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
    secureConnect.send(b'auth login\r\n')
    print(secureConnect.recv(1024))

    #login
    username = b"ebcperez@gmail.com"
    password = b"mypassword"
    secureConnect.send(base64.b64encode(username))
    secureConnect.send(b'\r\n')
    secureConnect.send(base64.b64encode(password))
    secureConnect.send(b'\r\n')
    recv_auth = secureConnect.recv(1024)
    print(recv_auth.decode())


    #send MAIL FROM
    secureConnect.send(b'MAIL FROM: <ebcperez@gmail.com>\r\n')
    data3 = secureConnect.recv(1024)
    print('MAIL FROM: ')
    print(data3)

    #send RCPT TO
    secureConnect.send(b'RCPT TO: <ebcperezcsc@gmail.com>\r\n')
    data4 = secureConnect.recv(1024)
    print('RCPT TO: ')
    print(data4)

    #send DATA
    secureConnect.send(b'DATA\r\n')
    data5 = secureConnect.recv(1024)
    print('DATA: ')
    print(data5)

    #send message data
    secureConnect.send(b'\r\n')
    secureConnect.send(b'SUBJECT: Test SMTP Email\nThis is an email sent with python sockets.\n.\r\n')
    data6 = secureConnect.recv(1024)
    print('Send data: ')
    print(data6)

    #message ends with single period
    secureConnect.send(b'.\r\n')
    data7 = secureConnect.recv(1024)
    print(data7)

    #send QUIT
    secureConnect.send(b'QUIT\r\n')
    print('Closing transmission.')
    secureConnect.close()

if __name__ == "__main__":
    main()
