import socket
from datetime import datetime
import cv2
import os

# file to write
file_to_write = 'other_files/billy.jpg'
# define host, port
link = ('',5002)
# create server socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# add socket options
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Bind connection
ss.bind(link)
# start server process
ss.listen(1)
# output information
print(f'[INFO]: listening on port {link[1]}. Server is waiting for connection.')

# accept connection to the client
conn, address = ss.accept()
print(f'[INFO]: Connected to client {address}')
# Get test data from client
test_data = conn.recv(1024)
print(f'[CLIENT]: {test_data.decode("utf-8")}')
# Response for receiving test data
conn.send(b'1')
# Receive the length of incoming file
img_size = int(conn.recv(1024).decode('utf-8'))
# Response
conn.send(b'1')

# Create a file to write the image
f = open(file_to_write,'wb')
# Define a counter
counter = 0
# Count time
time_checkpoint = datetime.now()
# Receive the image
while (counter < int(img_size) and (datetime.now() - time_checkpoint).seconds < img_size/10000):
    # Receive the data from client
    batch = conn.recv(512)
    # Save received data to file
    f.write(batch)
    # Update counter
    counter += len(batch)
    print(f'[INFO]: Received {counter} of {img_size} bytes of file')
# Send response from server
conn.send(b'Danke!')
# Don't forget to close the file
f.close()

# Check if the file transfer was successful
if img_size == os.path.getsize(file_to_write):
    print(f'[INFO]: Saved data to file \"{file_to_write}\". It lasted {datetime.now() - time_checkpoint}')
    print(f'[INFO]: Finished connection to client')
else:
    print(f'[ERROR]: File transfer failed!')

# Finish the connection
ss.close()
