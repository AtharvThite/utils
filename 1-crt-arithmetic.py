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

moduli = [103,109,113]   
M = 1
for m in moduli:
    M *= m
print(f"Moduli : {moduli}")
print(f"M = {M}")

while True:
    print("\n__Menu__")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = int(input("Enter the choice: "))

    if choice == 5:
        print("\nExiting")
        break

    A = int(input("\nEnter the first number : "))
    B = int(input("Enter the second number : "))

    a_moduli = []
    for mi in moduli:
        a_moduli.append(A % mi)

    b_moduli = []
    for mi in moduli:
        b_moduli.append(B % mi)

    if choice == 1:
        print("Addition : ")
        c_moduli = []
        for ai, bi, mi in zip(a_moduli, b_moduli, moduli):
            c = (ai + bi) % mi
            c_moduli.append(c)

    elif choice == 2:
        print("Subtraction : ")
        c_moduli = []
        for ai, bi, mi in zip(a_moduli, b_moduli, moduli):
            c = (ai - bi) % mi
            c_moduli.append(c)

    elif choice == 3:
        print("Multiplaction : ")
        c_moduli = []
        for ai, bi, mi in zip(a_moduli, b_moduli, moduli):
            c = (ai * bi) % mi
            c_moduli.append(c)

    elif choice == 4:
        print("Division : ")
        c_moduli = []
        for ai, bi, mi in zip(a_moduli, b_moduli, moduli):
            inv = mod_inverse(bi, mi)
            if inv is None:
                print(f"Division not possible in modulus {mi}")
                c_moduli.append(None)
            else:
                c_moduli.append((ai * inv) % mi)
                
    else:
        print("Invalid choice!")
        continue

    if None not in c_moduli:
        result = CRT(c_moduli, moduli)
        print(f"A moduli : {a_moduli}")
        print(f"B moduli : {b_moduli}")
        print(f"C moduli : {c_moduli}")
        print(f"Final Result = {result} (mod {M})")
    else:
        print("Error due to division")