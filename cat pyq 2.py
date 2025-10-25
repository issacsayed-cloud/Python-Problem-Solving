n=float(input("The charge of the atom is:"))
if n>0:
    print("Plus sign found")
    print(f"Magnitude:{n:+}")
else:
    print("Minus sign found")
    print(f"Magnitude:{n:-}")
print("Units: nC(nano-coloumbs)")