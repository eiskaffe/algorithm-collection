# https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html

def soe_naive(n: int) -> list:
    array = [True for _ in range(2, n+1)]
    for i in range(n-1):
        array[i+1:] = [
            True if (j+i+3) % (i+2) and b else False
            for j, b in enumerate(array[i+1:])
            ]
    print([x for x, b in zip(range(2, n+1), array) if b])

def soe(n: int) -> list:
    array = [True for _ in range(n+1)]
    array[0] = False
    array[1] = False
    for i in range(2, n+1):
        if array[i] and i*i <= n:
            for j in range(i*i, n+1, i):
                array[j] = False
    print([x for x, b in zip(range(n+1), array) if b])
    
# def linear_sieve(n: int) -> list:
#     lp: list = [0 for _ in range(n+1)]
#     pr: list = []
#     for i in range(2, n+1):
#         if lp[i] == 0:
#             lp[i] = i
#             pr.append(i)
#         for j in range(2, i*pr[j]):
#             lp[i * pr[j]] = pr[j]
#             if pr[j] == lp[i]:
#                 break
#     print(pr)