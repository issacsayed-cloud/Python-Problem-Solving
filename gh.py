typr_of_customer=input("Retail or Wholesale customers: ")
if typr_of_customer=="Retail customer":
    bill=int(input("Enter bill: "))
    if bill<1000:
        print("no discount is applied.");
        print("final amount:",bill)
    elif 1000<=bill<=5000:
        print("a 5% discount is applied.");
        bill1=bill-(bill*0.5);
        print("final amount:",bill1)
    elif bill>5000:
        print("a 10% discount is applied.");
        bill2=bill-(bill*0.1);
        print("final amount:",bill2)
elif typr_of_customer=="Wholesale customer":
    billl=int(input("Enter bill: "))
    if billl<5000:
        print("a 5% discount is applied.");
        billl1=billl-(billl*0.5);
        print("final amount:",billl1)
    elif 5000<=billl<=10000:
        print("a 10% discount is applied.");
        billl2=billl-(billl*0.1);
        print("final amount:",billl2)
    elif billl>10000:
        print("a 15% discount is applied.");
        bill3=billl-(billl*1.5);
        print("final amount:",bill3)