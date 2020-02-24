def searchRotatedArr(n, arr):
    if n < 1:
        return -1
    left = 0
    right = n - 1
    if arr[left] < arr[right]:
        return arr[0]
    while left < right:
        mid = (right-left)//2 + left
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        else:
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid -1
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(searchRotatedArr(n, arr))