a = "10.5"
b = 5
c = "7.5"

result = str(int(float(a) * float(c))) + str(b)
print("First result:", result)

result = int(float(a)) * int(b) + int(float(c))
print("Second result:", result)

final_result1 = int(result) / int(b)
final_result2 = str(result) + str(a)
final_result = final_result1 + float(final_result2)
print("Final result:", final_result)