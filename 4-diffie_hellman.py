# Diffie-Hellman Key Exchange

# Publicly known values (shared by both)
p = 23       # prime number
g = 5        # primitive root modulo p

# Private keys (chosen secretly by Alice and Bob)
a = 6        # Alice's private key
b = 15       # Bob's private key

# Compute public keys
A = pow(g, a, p)   # Alice sends A to Bob
B = pow(g, b, p)   # Bob sends B to Alice

# Compute shared secrets
secret_Alice = pow(B, a, p)
secret_Bob   = pow(A, b, p)

print("Public Prime p:", p)
print("Public Base g:", g)

print("\nAlice Private Key (a):", a)
print("Bob Private Key (b):", b)

print("\nAlice Public Key (A):", A)
print("Bob Public Key (B):", B)

print("\nShared Secret (Alice):", secret_Alice)
print("Shared Secret (Bob)  :", secret_Bob)
