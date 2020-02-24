def search(n, arr, target):
    def searchMinNum(n, arr):
        left = 0
        right = n - 1
        if arr[left] < arr[right]:
            return 0
        while left < right:
            index = (right - left) // 2 + left
            if arr[index] > arr[index + 1]:
                return index + 1
            else:
                if arr[index] > arr[right]:
                    left = index + 1
                else:
                    right = index - 1
    def biSearch(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return "Yes"
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return "No"


    if n < 1 or (n == 1 and arr[0] != target):
        return "No"
    index = searchMinNum(n, arr)
    if target > arr[n-1]:
        if index == 0:
            return "No"
        else:
            return biSearch(arr[0:index], target)
    elif target < arr[n-1]:
        return biSearch(arr[index:],target)
    else:
        return "Yes"

n, target = map(int, input().split())
arr = list(map(int, input().split()))
print(search(n, arr, target))