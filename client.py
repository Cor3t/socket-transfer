

import socket

# Create a socket object
client_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

# Connection to hostname on the port
client_socket.connect((host, 12345))

# File to send
file_name = "test.txt"

# Send file name to server
client_socket.send(file_name.encode())

# Open file in read mode
with open(file_name, 'rb') as f:
    # Read data from file and send to server
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.send(data)

print(f"File {file_name} sent successfully")

# Close the socket when done
client_socket.close()