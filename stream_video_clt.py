import os
import pickle
import socket
import struct
import numpy as np
import cv2

# Select video file to stream via socket
file_to_share = 0 #'/home/yurii/Desktop/motorhead_heroes.mp4'
# Initialize host and port
host = '10.1.0.176'
port = 8089

# Define client socket connection
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect to the host
clientsocket.connect((host,port))
# Send confirmation of connection to the server
clientsocket.send(bytes(clientsocket.getsockname()[0], 'utf-8'))
# Receive the response
first_response = clientsocket.recv(1024).decode('utf-8')
print(f'[INFO]: {first_response} to the host {host}:{port}')

# Send size of the video to the server and get response
filesize = bytes(str(os.path.getsize(file_to_share)),'utf-8')
clientsocket.send(filesize)
second_response = clientsocket.recv(1024).decode('utf-8')
print(f'[MSG]: {second_response}')

# capture the video
cap = cv2.VideoCapture(file_to_share)
# Read the frames from videofile/webcam
while True:
    ret,frame = cap.read()
    # convert data to the bytearray
    data = pickle.dumps(frame)
    # Send to the server
    clientsocket.sendall(struct.pack("L", len(data))+data)
