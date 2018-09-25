import socket
from time import sleep
host = '127.0.0.1'
port = 50001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host,port))
#First query
client_socket.send(b'Hey, lalka!')
# First answer
data = client_socket.recv(1024)
print(f'received {str(data)}')
counter = []

for i in range(3,100):

    # Second query
    data = bytes(str(i), 'utf-8')
    client_socket.send(data)

    # Second answer
    data = client_socket.recv(1024)
    print(f'Server converted {i} into {data.decode("utf-8")}')
    counter.append(data)
    sleep(1)
client_socket.close()
