n=int(input("Enter a number:"))
output_numbers=[]
for i in range(1,n+1):
    if i>15:
        break
    if i%2==0:
        continue
    output_numbers.append(i)
    string_numbers = [str(num)for num in output_numbers]
    output_string = ",".join(string_numbers)
print(f"Output:{output_string}")