class Solution:
    def getNumber(self, data):
        if len(data) < 1:
            return -1
        left = 0
        right = len(data-1)
        while left <= right:
            mid = (right - left)//2 + left
            if data[mid] == mid:
                return data[mid]
            elif data[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1