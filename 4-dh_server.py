import socket

# ---------------- Diffie-Hellman ----------------
p = 23   # prime number
g = 5    # primitive root

a = 6    # server's private key
A = pow(g, a, p)   # server's public key

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server waiting for client...")
conn, addr = s.accept()
print("Client connected:", addr)

# Send p, g, A to client
conn.send(f"{p},{g},{A}".encode())

# Receive client's public key B
B = int(conn.recv(1024).decode())
print("Received B from client:", B)

# Compute shared secret
shared_secret = pow(B, a, p)
print("Shared Secret (Server):", shared_secret)

conn.close()
s.close()
