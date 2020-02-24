def findLocalMin(arr):
    if len(arr) < 1:
        return -1
    if len(arr) == 1:
        return 0
    left = 0
    right = len(arr) - 1
    n = len(arr)
    while left < right:
        mid = (right - left)//2 + left
        if (mid == 0 and arr[mid] < arr[mid+1]) or (mid == n-1 and arr[mid-1] > arr[mid])\
                or (arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]):
            return mid
        elif arr[mid] < arr[mid+1]:
            right = mid -1
        else:
            left = mid+1
    if left == 0 or left == n-1:
        return left
    return -1
n = int(input())
arr = list(map(int, input().split()))
print(findLocalMin(arr))

