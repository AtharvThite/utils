import socket

# Client's private key
b = 15   

s = socket.socket()
s.connect(("localhost", 5000))

# Receive p, g, A from server
data = s.recv(1024).decode()
p, g, A = map(int, data.split(","))

# Compute client's public key B
B = pow(g, b, p)

# Send B to server
s.send(str(B).encode())

# Compute shared secret
shared_secret = pow(A, b, p)

s.close()
