# Server.py
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8080

# Bind to the port
s.bind(('', port))

# Wait for client connection
s.listen(1)
print("Server started")
print("Waiting for client request..")

# Establish connection with client
c, addr = s.accept()
print("Connected client :", addr)

# A function to calculate the sum of digits of a number
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# A loop to receive data from client and send back the result
while True:
    # Receive data from client
    data = c.recv(1024)
    # Decode the data
    data = data.decode()
    # Convert the data to integer
    num = int(data)
    # Calculate the sum of digits
    result = sum_digits(num)
    # Convert the result to string
    result = str(result)
    # Encode the result
    result = result.encode()
    # Send the result back to client
    c.send(result)

# Close the connection
c.close()
