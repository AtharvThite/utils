def mod_inverse(a,m):
    a = a%m
    for x in range(1,m):
        if (x*a)%m == 1:
            return x
    return None

def CRT(a, m):
    M = 1
    for mi in m:
        M *= mi
    x = 0
    for ai, mi in zip(a,m):
        Mi = M // mi
        Minv = mod_inverse(Mi, mi)
        x += ai * Mi * Minv
    return x % M

a = [2, 3, 2]
m = [3, 5, 7]

result = CRT(a, m)
print("Solution x =", result)
