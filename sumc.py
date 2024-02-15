# Client.py
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8080

# Connect to the server on local computer
s.connect(('127.0.0.1', port))

# A loop to take input from user and send to server
while True:
    # Take input from user
    data = input("Enter a number: ")
    # Encode the data
    data = data.encode()
    # Send the data to server
    s.send(data)
    # Receive the result from server
    result = s.recv(1024)
    # Decode the result
    result = result.decode()
    # Print the result
    print("Sum of digits is " + result)
    # Check if user wants to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice == 'n':
        break

# Close the socket
s.close()
