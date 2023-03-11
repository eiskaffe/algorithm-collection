N = int(input())
szotar = {}
for i, datum in enumerate(input().split()): # O(N)
    szotar[datum] = i+1     # O(1)
print(min(szotar.values())) # O(N)
# -> O(2*N)  ==>  O(N)
