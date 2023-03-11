N = int(input())

def ritka(n):
    binary_n = bin(n)[2:]
    return "11" not in binary_n

i = 0
c = 0
while c < N:
    if ritka(i):
        c += 1
    i += 1
print(i-1)
