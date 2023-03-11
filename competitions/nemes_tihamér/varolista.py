N = int(input())

prefixSum = [0]*(N*2+1)
for i in range(1, N):
    prefixSum[i] = 