# https://cp-algorithms.com/algebra/divisors.html#number-of-divisors
from typing import List

def number_of_divisors(*exponents: int) -> int:
    # (α1 + 1)(α2 + 1)...(αk + 1)
    result: int = 1
    for exp in exponents:
        result *= (exp + 1)
    return result

def sum_of_divisiors(primes: List[tuple]):
    result: int = 1
    for prime, exponent in primes:
        result *= (prime ** (exponent + 1) - 1) / (prime - 1)
    return result