toc = input("Enter customer type(retail/wholesale):")
pa = int(input("Enter the purchase amount:"))
li = input("Customer is a member of supermarket's loyality program(yes/no):")
if toc=="retail":
    if li=="no":
        if pa<1000:
            print("no discount is available")
        elif 1000<=pa<=5000:
            print("a 5% discount is available")
            pa_ad=pa-(pa*0.05)
            print("The final amount after applying discount:",pa_ad)
        elif pa>5000:
            print("a 10% discount is available")
            pa_ad1=pa-(pa*0.1)
            print("The final amount after applying discount:",pa_ad1)
    if li=="yes":
        if pa<1000:
            print("a 2% loyality discount is available")
            pa_ad2=pa-(pa*0.02)
            print("The final amount after applying discount:",pa_ad2)
        elif 1000<=pa<=5000:
            print("a 5% + (2%loyality) discount is available")
            pa_ad3=pa-(pa*0.07)
            print("The final amount after applying discount:",pa_ad3)
        elif pa>5000:
            print("a 10% + (2%loyality) discount is available")
            pa_ad4=pa-(pa*0.12)
            print("The final amount after applying discount:",pa_ad4)
elif toc=="wholesale":
    if li=="yes":
        if pa<5000:
            print("a 5% + (2%loyality) discount is available")
            pa_ad5=pa-(pa*0.07)
            print("The final amount after applying discount:",pa_ad5)
        elif 5000<=pa<=10000:
            print("a 10% + (2%loyality) discount is available")
            pa_ad6=pa-(pa*0.12)
            print("The final amount after applying discount:",pa_ad6)
        elif pa>10000:
            print("a 15% + (2%loyality) discount is available")
            pa_ad7=pa-(pa*0.17)
            print("The final amount after applying discount:",pa_ad7)
    elif li=="no":
        if pa<5000:
            print("a 5% discount is available")
            pa_ad8=pa-(pa*0.05)
            print("The final amount after applying discount:",pa_ad8)
        elif 5000<=pa<=10000:
            print("a 10% discount is available")
            pa_ad9=pa-(pa*0.1)
            print("The final amount after applying discount:",pa_ad9)
        elif pa>10000:
            print("a 15% discount is available")
            pa_ad10=pa-(pa*0.15)
            print("The final amount after applying discount:",pa_ad10)