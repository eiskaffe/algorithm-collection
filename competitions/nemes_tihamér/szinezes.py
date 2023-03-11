# import timeit_decorator

N, Q = input().split()
N = int(N)
Q = int(Q)
sorozat = [int(x) for x in input()]
# from random import randint
# sorozat = [x % 2 for x in range(200_000)]
# questionaires = [randint(0, N-1) for _ in range(Q)]
# sorozat = [0, 1, 0, 0, 1]

new_list = []
current_item = sorozat[0]
for val in sorozat:
    if val != current_item:
        new_list.append(current_item)
        current_item = val
new_list.append(val)

p = len([x for x in new_list if x])
k = len(new_list) - p
solution = min(p, k)
print(solution)

# for q in range(Q):
for i in questionaires:
    # i = int(input()) - 1
    curr = sorozat[i]
    if N-1 > i > 0:
        if sorozat[i-1] != curr and sorozat[i+1] != curr:
            print(solution - 1)
        elif sorozat[i-1] == curr and sorozat[i+1] == curr:
            print(solution + 1)
    elif i == N-1:
        if sorozat[i-1] != curr:
            print(solution - 1)
        else:
            print(solution + 1)
    elif i == 0:
        if sorozat[i+1] != curr:
            print(solution - 1)
        else:
            print(solution + 1)

# i = 2
# 1 0 1 0 1; p=3, k=2 -> 1 0 0 0 1, azaz p=2, k=1 ==> p-1; k-1
# 1 0 0 0 1; p=2, k=1 -> 1 0 1 0 1, azaz p=3, k=2 ==> p+1; k+1
# 0 1 0 1 0; p=2, k=3 -> 0 1 1 1 0, azaz p=1, k=2 ==> p-1; k-1
# 0 1 1 1 0; p=1, k=2 -> 0 1 0 1 0, azaz p=2, k=3 ==> p+1; k+1