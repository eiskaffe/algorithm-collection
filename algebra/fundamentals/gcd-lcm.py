# https://cp-algorithms.com/algebra/euclid-algorithm.html#algorithm

def gcd_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd_recursive (b, a % b)

def gcd(a: int, b: int) -> int:
    while b:
        a %= b
        a, b = b, a
    return a

def lcm(a: int, b: int) -> int:
    return (a * b) / gcd(a, b) 

# def gcd_optimization(a: int, b: int) -> int:
#     if not (a and b): # <=> (not a) or (not b) <=> a == 0 or b == 0
#         return a | b
#     shift = 