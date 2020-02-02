# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) < 1:
            return 0
        left = 0
        right = len(data) - 1
        first, last = 0, 0
        while left <= right:
            mid = (right - left)//2 + left
            if data[mid] == k:
                if (mid > 0 and data[mid - 1] != k) or mid == 0:
                    first = mid
                    break
                else:
                    right = mid - 1
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1

        left = first
        right = len(data) - 1
        while left <= right:
            mid = (right - left)//2 + left
            if data[mid] == k:
                if (mid < len(data) - 1 and data[mid + 1] != k) or mid == len(data) - 1:
                    last = mid
                    break
                else:
                    left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        if first == 0 and last == 0 and data[0] != k:
            return 0
        return last - first + 1


data = [1, 2, 3, 3, 3, 3, 4, 5]
print(Solution().GetNumberOfK(data, 3))
