# Also works in conjunction with share_a_pic_clt.py as the client
import socket
from datetime import datetime
import os
import cv2
#from flask import Flask
import numpy as np

# flask app
#app = Flask(__name__)

#@app.route('/')
#def stream():
    # host and port
host = '0.0.0.0'
port = 5002

# create socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# add socket properties
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the connection
ss.bind((host, port))
# make port listen
ss.listen()
print(f'[INFO]: server is listening on port {port}')
# wait until client is connected
connection, address = ss.accept()

# Receive test data from client
test_data = connection.recv(1024).decode('utf-8')
print(f'[MSG]: {test_data}')
# Send
connection.send(b'Hi, client! I am the server')
# Get size of the video file from client
file_size = int(connection.recv(1024).decode('utf-8'))
# Give a response
connection.send(b'OK')
# Define counter to count transferred bytes
bytes_sent = 0
# Empty bytearray to fill it with bytes later
bytes = bytearray()
# Start counting time
time_checkpoint = datetime.now()
# Start streaming
while bytes_sent < file_size and (datetime.now() - time_checkpoint).seconds < bytes_sent/10000:
    # Get bunches of data
    batch = connection.recv(512)
    # Add bytes to bytearray
    bytes += batch
    # Find the first and the last byte for every frame
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    # Update counter
    bytes_sent += len(batch)
    print(f'[INFO]: received {bytes} of {img_size} bytes of data')

    if a != -1 and b != -1:
        print('shown')
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        frame = np.asarray(bytearray(bytes), dtype=np.uint8)
        cv2.imshow('kek', frame)#, cv2.IMREAD_COLOR)
        #print(type(i))

    #    cv2.imshow('joj', i)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            capture.release()
            break
    #cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5168)"""
