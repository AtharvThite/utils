def multiplicative_inverse(a,b):
    if a<b: a,b=b,a
    r1,r2 = a,b
    t1,t2 = 0,1
    print("Euclidean Algorithm for GCD and MI : ")
    print("-"*40)
    print(f"{'q':<5} {'r1':<8} {'r2':<8} {'r':<8} {'t1':<8} {'t2':<8} {'t':<8}")
    print("-"*40)
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        t = t1 - (t2*q)
        print(f"{q: <5} {r1: <8} {r2: <8} {r: <8} {t1: <8} {t2: <8} {t: <8}")
        r1,r2 = r2,r
        t1,t2 = t2,t
    print(f"GCD of {a} and {b} = {r1}")
    print(f"Multiplicative Invverse of {a} and {b} = {t1}")

multiplicative_inverse(3,11)