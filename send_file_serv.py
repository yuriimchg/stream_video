import socket
import os
# file to write
file_to_write = 'text_files/received.txt'
# define host, port
link = ('',5002)
# create server socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Bind connection
ss.bind(link)
# start server process
ss.listen(1)
# Update information
print(f'[INFO]: listening on port {link[1]}. Server is waiting for connection.')

# accept connection to the client
conn, address = ss.accept()
print(f'[INFO]: Connected to client {address}')
# Get test data from client
test_data = conn.recv(1024)
print(f'[CLIENT]: {test_data.decode("utf-8")}')
# Response
conn.send(b'1')
# Create a file to write
f = open(file_to_write,'wb')
# Receive the data from client
data = conn.recv(1024)
# Check if received data is not None
if data and len(data) > 0:
    # Save received data to file
    f.write(data)
    print(f'[INFO]: Saved data to file \"{file_to_write}\"')
else:
    print('[ERROR]: Failed to receive data.')
# Response to client
print(f'[INFO]: Finished connection to client')
conn.send(b'Danke!')
# Don't forget to close the file
f.close()
# Finish the connection
ss.close()
