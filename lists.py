def is_prime(d):
    if d < 2:
        return False
    for i in range(2, d):
        if d % i == 0:
            return False
    return True

def sum_prime(num):
    s = 0
    while num > 0:
        d = num % 10
        if is_prime(d):
            s += d
        num //= 10
    return s

def sum_composite(num):
    s = 0
    while num > 0:
        d = num % 10
        if d > 1 and not is_prime(d):
            s += d
        num //= 10
    return s

n = int(input("Enter number: "))
prime_sum = sum_prime(n)
comp_sum = sum_composite(n)
print("Difference:", comp_sum - prime_sum)
