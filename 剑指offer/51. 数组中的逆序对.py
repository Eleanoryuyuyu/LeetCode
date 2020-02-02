# -*- coding:utf-8 -*-
class Solution:
    # 1. 使用一个copy数组排好序，在原数组中每次查找copy数组最小值得index，因为是最小值，所以它之前有多少个数就有多少个逆序对；
    # 然后每次在原数组中删去这个数。
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        count = 0
        for i in copy:
            count += data.index(i)
            if count > 1000000007:
                count = count % 1000000007
            data.remove(i)
        return count % 1000000007

    # 2. 归并排序思想
    def InversePairs2(self, data):
        if len(data) <= 1:
            return 0
        start = 0
        end = len(data)
        ans = self.mergeSort(data, start, end)
        return ans % 1000000007

    def mergeSort(self, data, start, end):
        if start == end - 1:
            return 0
        mid = (end + start)//2
        left_count = self.mergeSort(data, start, mid)
        right_count = self.mergeSort(data, mid, end)
        merge_count = self.merge(data, start, mid, end)
        return left_count + right_count + merge_count

    def merge(self, data, start, mid, end):
        tmp = []
        i = start
        j = mid
        count = 0
        while i < mid and j < end:
            if data[i] <= data[j]:
                tmp.append(data[i])
                i += 1
            else:
                tmp.append(data[j])
                j += 1
                count += mid - i
        while i < mid:
            tmp.append(data[i])
            i += 1
        while j < end:
            tmp.append(data[j])
            j += 1
        data[start:end] = tmp
        del tmp
        return count % 1000000007


data = [7, 5, 6, 4]
print(Solution().InversePairs2(data))
