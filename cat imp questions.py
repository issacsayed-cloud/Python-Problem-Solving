choice=input("Enter pattern P1 or P2:")
if choice=="P1":
    n=4
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print(i,end=" ")
        print()
elif choice=="P2":
    n=4
    for i in range(1,n+1):
        for j in range(i):
            print(".",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print(".",end=" ")
        print()
else:
    print("Not a Valid pattern")