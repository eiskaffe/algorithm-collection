def trial_divison(n: int) -> list:
    from math import sqrt, floor
    factorization: list = []
    for d in range(2, floor(sqrt(n))+1):
        while n % d == 0:
            factorization.append(d)
            n //= d
    if n > 1:
        factorization.append(n)
    return factorization

def wheel_divison(n: int) -> list:
    # optimization of the previous
    # this can be extended to m number of precomputed primes
    from math import sqrt, floor
    factorization: list = []
    while n % 2 == 0:
        factorization.append(2)
        n //= 2
    
    for d in range(3, floor(sqrt(n))+1, 2):
        while n % d == 0:
            factorization.append(d)
            n //= d
    if n > 1:
        factorization.append(n)
    return factorization

def fermat(n: int) -> int:
    from math import ceil, sqrt
    a = ceil(sqrt(n))
    b2 = a*a - n
    b = round(sqrt(b2))
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = round(sqrt(b2))
    return a-b
