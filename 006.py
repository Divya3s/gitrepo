# 6. Factorial of a Number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120

def f(n):
    r =1
    for i in range(2, n+1):
        r = r*i
    return r

print(f(7))