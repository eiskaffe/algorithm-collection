from math import factorial

N = int(input())

# no three longs
result = 2 ** N
for i in range(1, N // 3 + 1):
    s = (N - i*3)
    k = i + s
    print(k, i, s)
    result += 2 ** k * (factorial(k) // factorial(i)*factorial(s))
print(result % 20210108)