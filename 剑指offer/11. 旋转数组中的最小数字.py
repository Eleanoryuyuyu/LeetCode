# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        mid = low  # mid 初始化0的原因：把数组前0个元素移到末尾，此时数组是一个非递减数组，最小值即为第一个
        while rotateArray[low] >= rotateArray[high]:
            # 第一个指针会指向前段数组的最后一个元素，第二个指针会指向后段数组的第一个元素
            if high - low == 1:
                mid = high
                break
            mid = (high - low)//2 + low
            if rotateArray[mid] >= rotateArray[high]:
                low = mid
            elif rotateArray[mid] <= rotateArray[low]:
                high = mid
        return rotateArray[mid]

array = [3,4,5,1,2]
print(Solution().minNumberInRotateArray(array))