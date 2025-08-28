# 5. Fibonacci Series (First N Numbers)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)  # Output: 0 1 1 2 3
print()
def fb(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a+b

fb(6)