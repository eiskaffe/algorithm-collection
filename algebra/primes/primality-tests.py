# https://cp-algorithms.com/algebra/primality_tests.html

def trial_division(x: int) -> bool:
    from math import sqrt, floor
    for d in range(2, floor(sqrt(x))+1):
        print("cock")
        if x % d == 0:
            return False
    return True

def probablyPrimeFermat(n: int, iter: int = 5) -> bool:
    from random import randint
    if n < 4:
        return n == 2 or n == 3
    for i in range(iter):
        a = 2 + randint(2, n*n) % (n - 3)
        if pow(a, n - 1, n) != 1:
            return False
    return True

print(probablyPrimeFermat(797))