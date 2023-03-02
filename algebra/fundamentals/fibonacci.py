def fib(n: int) -> int:
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n: int) -> int:
    if n == 0 or n == 1: 
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)