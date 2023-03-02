N = int(input())
array = list(map(int, input().split()))
# array = [500_000-i for i in range(500_000)]

# O(n^2)
most_distance = 0
indexes = None
for i, x in enumerate(array):
    for j, y in enumerate(array[i+1:]):
        if x > y and most_distance < j+1:
            most_distance = j+1-i
            indexes = (i+1, i+j+2)
print(-1 if indexes is None else " ".join(indexes))


# O(n)
# most_distance = 0
# indexes = None
# for x in range(N, 1, -1):
#     for j, y in enumerate(array[-1::-1]):
#         if x == y: break
#         if x > y:
#             if most_distance < N-j - i:
#                 most_distance = N-j - i
#                 indexes = (i+1, N-j)
        

# print(indexes)