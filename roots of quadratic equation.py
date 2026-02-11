a = int(input("Enter the coefficent a: "))
b = int(input("Enter the coefficent b: "))
c = int(input("Enter the coefficent c: "))
det = b*b - 4*a*c
if a == 0:
    print("It is not a quadratic equation.")
else:
    if det > 0:
        print("there are two real and distinct roots.")
    elif det < 0:
        print("there are two complex roots.")
    else:
        print("there i s one real root.")