import socket

# If host is an empty string, then host is this PC.
host = ''
port = 50001

# AF_INET and SOCK_STREAM are constants, telling the system which protocols to use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Associate the connection with the specific port. Just connect this host to this port
s.bind((host,port))
# Start the server process, this programm accepting connections when asked
s.listen()

print(f'listening on port {port}')
# conn represents the connection and is used to send and receive data
conn, addr = s.accept()

print(f'Connected to {addr}')
# First query
data = conn.recv(1024)
print(f'server received such data: {data}')
# First answer
conn.send(b'Hey, you, I am the host')

while True:
    # Second query
    data = conn.recv(1024)
    # Read the incoming data
    if data:
        i = data.decode('utf-8')
        # Convert it to integer
        print("Received ", i, 'yes')

        # Work with data
        # Square it and convert to bytes
        sq_i = str(int(i) ** 2)
        data = bytes(str(sq_i), 'utf-8')
        print(f'converted {i} into {sq_i}')
        # Send to the client
        # Second answer
        conn.send(data)
        print(f'sent data #{i}')
conn.close()
