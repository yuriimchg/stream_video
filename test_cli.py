import socket
from time import sleep

# define host and port

host = '127.0.0.1'
port = 5678
# AF_INET and SOCK_STREAM are just telling which protocol is used by socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect host to the port
client_socket.connect((host,port))
#First query
client_socket.send(b'Hey, server!')
# First answer
data = client_socket.recv(1024)
print(f'received {str(data)}')

for i in range(100):

    # Send data to the server
    data = bytes(str(i), 'utf-8')
    client_socket.send(data)

    # Get answer
    data = client_socket.recv(1024)
    print(f'Server converted {i} into {data.decode("utf-8")}')
# Close client socket. Goodbye!
client_socket.close()
