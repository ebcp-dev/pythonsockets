#Socket programming 2
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((TCP_IP, TCP_PORT))
serverSocket.listen(1)
print('Server listening on: {}:{}'.format(TCP_IP, TCP_PORT))

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Connection adress: {}'.format(addr))
    request = connectionSocket.recv(BUFFER_SIZE)
    print(request.split())
    filename = request.split()[1]
    if not request:
        break
    print('Server received data: {}'.format(request))

    try:
        file = open(filename[1:])

        #send headers
        connectionSocket.send(b'HTTP/1.1 200 OK\n')
        connectionSocket.send(b'Content-Type: text/html\n')
        connectionSocket.send(b'\n')
        #send file
        connectionSocket.send(file.read().encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send(b'HTTP/1.1 404 Not Found\n')
        connectionSocket.send(b'Content-Type: text/html\n\n')
        #show 404 message in browser
        connectionSocket.send(b'''
            <html>
                <h1>404 File not found</h1>
            </html>
        ''')
        connectionSocket.close()
        
