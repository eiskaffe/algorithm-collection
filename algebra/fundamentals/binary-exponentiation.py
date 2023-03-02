#https://cp-algorithms.com/algebra/binary-exp.html#implementation

def linear_method(a: int, b: int) -> int:
    # O(n)
    result = 1
    for _ in range(b):
        result *= a
    return result

def binpow(a: int, b: int) -> int:
    # O(log n)
    result: int = 1
    while b > 0:
        if b & 1:
            result *= a
        a *= a
        b >>= 1
    return result

# EXAMPLE CASES
def example1(a, b, m):
    # Compute x^n mod m!
    a %= m
    result = 1
    while b > 0:
        if b & 1:
            result = result * a % m 
        a = a * a % m
        b >>= m
    return result