def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Now you have to call the function
#you can choose any value of n, let say 5
fact = factorial(5)
print(fact)