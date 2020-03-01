def search(nums, target):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if (mid == 0 and nums[mid] > target) or (nums[mid - 1] <= target and nums[mid] > target):
            return nums[mid]
        elif nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [1, 3, 4, 5, 6, 7, 8]
target = 0
print(search(nums, target))
