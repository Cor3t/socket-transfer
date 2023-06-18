import socket

# Create a socket object
server_socket = socket.socket()

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to the port
server_socket.bind((host, port))

# Become a server socket
server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")
    
    # Receive file name from client
    file_name = client_socket.recv(1024).decode()
    
    # Open file in write mode
    with open(file_name, 'wb') as f:
        # Receive data from client and write to file
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    
    print(f"File {file_name} received successfully")
    
    # Close the connection with the client
    client_socket.close()
