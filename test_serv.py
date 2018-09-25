import socket
from random import randint
from datetime import datetime

# If host is an empty string, then this PC would be a host.
host = '0.0.0.0'
port = 5678

# AF_INET and SOCK_STREAM are constants, telling the system which protocols to use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Associate the connection with the specific port.
# Simply connect this host to that port
s.bind((host,port))
# Start the server process, this programm accepting connections when asked
s.listen(1)

print(f'listening on port {port}. Waiting for connection')
# conn represents the connection and is used to send and receive data
conn, addr = s.accept()
print(f'Connected to {addr}')

# First query
data = conn.recv(1024)
print(f'server received such data: {data}')

# First answer
conn.send(b'What?')

# Make server wait for client requests
while True:
    # Receive query
    data = conn.recv(1024)
    # Read the incoming data
    if data:
        # set datetime checkpoint
        chkpt = datetime.now()
        # decode bytes
        i = data.decode('utf-8')
        # Work with data
        sq_i = str(int(i) ** randint(1,6))
        # Encode data
        data = bytes(str(sq_i), 'utf-8')
        print(f'Received {i}, converted it into {sq_i}')
        # Send encoded data to the client
        conn.send(data)
        print(f'sent data #{i} to client.')

    if not data and (datetime.now() - chkpt).seconds ==5:
        s.listen(1)
        print(f'listening on port {port}. Waiting for connection.')

        conn, addr = s.accept()
        print(f'Connected to {addr}')
        data = conn.recv(1024)
        print(f'server received such data: {data}')

        # First answer
        conn.send(b'What?')
conn.close()
