def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 32
b = 120
result = gcd(a, b)
print(result)