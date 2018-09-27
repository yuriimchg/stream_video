import socket
import os
import cv2

# file to share
file_to_share = 'other_files/bill_murray1.jpg'
# host and port
host = '127.0.0.1'
port = 5002
# create client socket
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the port
cli_socket.connect((host,port))
print(f'[INFO]: Connected to the host {host}')
# Confirm connection to the server
cli_socket.send(b'Hi, server! I\'ve got something for you!')
# Get response from server
print(f'[MSG]:{cli_socket.recv(1024).decode("utf-8")}')
# get size of the image
img_size = os.path.getsize(file_to_share)
img_size = bytes(str(img_size), "utf-8")
# Send size of the image to server
cli_socket.send(img_size)
# Receive response from server
cli_socket.recv(1024)
# Try to send every line of the file
f = open(file_to_share, 'rb')
while True:
    batch = f.readline(512)
    if not batch:
        break
    cli_socket.send(batch)
f.close()
print(f'[INFO]: Sent file to server, waiting for response')

# Get response from server
data = cli_socket.recv(1024)
print(f'[MSG]:{data.decode("utf-8")}')

cli_socket.close()
print('[INFO]: Closed connection')
