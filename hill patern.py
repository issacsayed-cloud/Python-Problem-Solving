n = int(input("Enter the length of the pattern:"))
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for p in range(i):
        print("*",end=" ")
    print()