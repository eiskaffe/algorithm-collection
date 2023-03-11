def build_prefix_sum(arr) -> list:
    prefixSum = [0]*(len(arr)+1)
    for i, val in enumerate(arr, 1):
        prefixSum[i] = prefixSum[i-1] + val
    return prefixSum

def build_prefix_sum_(arr) -> list:
    prefixSum = [0]
    current = 0
    for val in arr:
        current += val
        prefixSum.append(current)
    return prefixSum

def calculate_prefix_sum_slice(prefixSum: list, start: int, end: int) -> int:
    return prefixSum[end + 1] - prefixSum[start]

print(build_prefix_sum_([1, 4, 5]))


# [2, 4, 3] --> [0, 2, 6, 9]
#  0  1  2      
#  ==> 0 = [0, 4] -> [0, 1, 2]
#      1 = [5, 6] -> [3, 4, 5, 6]
#      2 = [7, 9] -> [7, 8, 9]
    
    