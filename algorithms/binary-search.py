def binarySearch(arr: list, x: int) -> int:
    high = len(arr)
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1