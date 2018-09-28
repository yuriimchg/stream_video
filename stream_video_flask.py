from flask import Flask, Response
import socket
import pickle
import numpy as np
import cv2

host = '127.0.0.1'
port = 5003
app = Flask(__name__)

@app.route('/')
def hi():
    return('Go away')

@app.route('/video')
def wrap_streaming():
    return Response(stream_video(host,port), mimetype='multipart/x-mixed-replace; boundary=frame')
def stream_video(host,port):
    """
    Video Streaming function
    """
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Connect host to the port
    s.bind((host,port))
    # Make server listen on port {port_id}
    s.listen(1)
    print(f'[INFO]: Server is listening on port {port}.')
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
    print(f'[INFO]: Ready to stream video from client')
    # Send a response to the client
    conn.send(bytes(f'Server is ready to stream video of size {video_size}', 'utf-8'))

    # Start receiving video streaming
    while True:
        # Receive data until size of the received data is equal to the size of the video
        while len(data) < video_size:
            # Update bytearray with video streaming from client
            data += conn.recv(4096)
        # Split the bytearray
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
        frame = pickle.loads(frame_data)
        # Show the frame of the video from client
        yield cv2.imshow('frame',frame)
        yield cv2.waitKey(1)



if __name__ == '__main__':
    app.run(host,port, debug=True, threaded=True)
