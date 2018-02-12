#TCP server
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
NOT_FOUND = "404 Not Found"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("TCP server running on: {}:{}".format(TCP_IP, TCP_PORT))

conn, addr = s.accept()
print('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print('Received data(server):', data)
    conn.send(data) #echo
conn.close()
