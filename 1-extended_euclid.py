def extended_euclid(a,b):
    if a < b : a,b = b,a
    r1,r2 = a,b
    t1,t2 = 0,1
    s1,s2 = 1,0
    print("Extended Euclidean Algorithm for GCD and (s,t) pair : ")
    print("-"*50)
    print(f"{'q':<5} {'r1':<8} {'r2':<8} {'r':<8} {'s1':<8} {'s2':<8} {'s':<8} {'t1':<8} {'t2':<8} {'t':<8}")
    print("-"*50)
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - (t2*q)
        s = s1 - (s2*q)
        print(f"{q: <5} {r1: <8} {r2: <8} {r: <8} {s1: <8} {s2: <8} {s: <8} {t1: <8} {t2: <8} {t: <8}")
        r1,r2 = r2,r
        s1,s2 = s2,s
        t1,t2 = t2,t

    print(f"GCD({a}, {b} = {r1}) | s = {s1} | t = {t1}")

extended_euclid(28,161)