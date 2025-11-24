def basic_euclid(a, b):
    if a < b : a,b = b,a
    r1 = a
    r2 = b
    print("Basic Euclidean Algorithm for GCD : ")
    print("-"*25)
    print(f"{'q':<5} {'r1':<5} {'r2':<5} {'r':<5}")
    print("-"*25)
    while r2 != 0:
        q = r1 // r2
        r = r1 % r2
        r1, r2 = r2, r
        print(f"{q:<5} {r1:<5} {r2:<5} {r:<5}")
    print("-"*25)
    print(f"GCD of {a} and {b} = {r1}")

basic_euclid(15,10)