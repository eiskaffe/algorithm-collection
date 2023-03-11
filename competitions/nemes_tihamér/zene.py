N, K = input().split()
N = int(N)
K = int(K)
hosszok = [int(x) for x in input().split()]

prefixSum = [0]*(N+1)
total = 0
# O(N)
for i, val in enumerate(hosszok, 1):
    prefixSum[i] = prefixSum[i-1] + val
    total += val

# O(K)
for p in input().split():
    high = N
    low = 0
    p = int(p) % total + 1
    # binary search, guarnteed to find => O(log N)
    while True:
        mid = (low + high) // 2
        if prefixSum[mid] < p <= prefixSum[mid+1]:
            print(p, mid+1)
            break
        elif prefixSum[mid] < p:
            low = mid + 1
        else:
            high = mid - 1
            
# ==> O(N + K*log(N))
            