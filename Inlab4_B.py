def multiply(m, n):
    if (n <= 1):
        return m
    else:
        return m + multiply(m, n - 1)
mul = multiply(10,5)
print(mul)
