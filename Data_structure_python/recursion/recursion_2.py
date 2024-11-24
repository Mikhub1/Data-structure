def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return power(base, exponent/2)**2
    else:
        return base * power(base, exponent-1)

#Just pass base and exponent as an argument to this function
#And it will find the power
#Now let's pass 2 as base and 3 as an exponent

base = 2
exponent = 3
result = power(base, exponent)
print(result)