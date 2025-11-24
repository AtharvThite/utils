import socket

# Client's private key
b = 15    # client's private key

s = socket.socket()
s.connect(("localhost", 5000))

# Receive p, g, A from server
data = s.recv(1024).decode()
p, g, A = map(int, data.split(","))
print("Received from server:")
print("p =", p, "g =", g, "A =", A)

# Compute client's public key B
B = pow(g, b, p)
print("Client public key B:", B)

# Send B to server
s.send(str(B).encode())

# Compute shared secret
shared_secret = pow(A, b, p)
print("Shared Secret (Client):", shared_secret)

s.close()
