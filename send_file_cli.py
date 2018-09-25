import socket
import os

# file to share
file_to_share = 'text_files/clone.txt'
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
cli_socket.recv(1024)
# It is time to share file
f = open(file_to_share,'rb')
# Split file into lines
try:
    # Try to send every line of the file
    cli_socket.send(f.read())
    print(f'[INFO]: Sent file to server, waiting for response')
    # Get response from server
    data = cli_socket.recv(1024)
    print(f'[MSG]:{data.decode("utf-8")}')
except:
    # Show error message in case of failure
    print('[ERROR]: Failed to send data')
finally:
    f.close()
cli_socket.close()
