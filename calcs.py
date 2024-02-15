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

# A function to perform basic arithmetic operations
def calculate(op, x, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "Invalid operator"

# A loop to receive data from client and send back the result
while True:
    # Receive data from client
    data = c.recv(1024)
    # Decode the data
    data = data.decode()
    # Split the data into operator and operands
    op, x, y = data.split()
    # Convert the operands to integers
    x = int(x)
    y = int(y)
    # Perform the calculation
    result = calculate(op, x, y)
    # Convert the result to string
    result = str(result)
    # Encode the result
    result = result.encode()
    # Send the result back to client
    c.send(result)

# Close the connection
c.close()
