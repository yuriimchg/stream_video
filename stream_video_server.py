import cv2
import pickle
import numpy as np
import socket
import struct


# Define host and port
host=''
port=8089
# Define socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created')
# Connect host to the port
s.bind((host,port))
print('Socket bind complete')
# Make server listen on port {port_id}
s.listen(1)
print('Socket now listening')
# Wait until client is connected
conn,addr=s.accept()

# Get message from the
first_msg = conn.recv(1024).decode('utf-8')
print(f'[INFO]: New connection from {first_msg}')
# Send a response
conn.send(b'Accepted connection.')
# Get the size of the incoming video
video_size = int(conn.recv(1024).decode('utf-8'))
video_size = struct.calcsize("L")
# Initialize empty bytearray. It will be filled with the bytes of video streaming
data = b""
# Send a response to the client
conn.send(bytes(f'Server is ready to stream video of size {video_size}', 'utf-8'))

# Start receiving video streaming
while True:
    # Receive data until size of the received data is equal to the size of the video
    while len(data) <  video_size:
        # Update bytearray with video streaming from client
        data += conn.recv(4096)
    #
    packed_msg_size = data[:video_size]
    data = data[video_size:]
    # Get the size of a single frame
    msg_size = struct.unpack("L", packed_msg_size)[0]
    # Get the single frame
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Convert the frame from bytes type
    frame=pickle.loads(frame_data)
    # Show the frame of the video from client
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
