class Solution:
    def getMissingNumber(self, data):
        if len(data) < 1:
            return -1
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if data[mid] == mid:
                left = mid + 1
            else:
                if (mid > 0 and data[mid - 1] == mid - 1) or mid == 0:
                    return data[mid]
                elif mid > 0 and data[mid - 1] != mid - 1:
                    right = mid - 1
        return -1

data = [0,1,2,5,3,4]
print(Solution().getMissingNumber(data))