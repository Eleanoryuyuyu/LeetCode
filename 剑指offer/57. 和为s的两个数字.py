# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        array_dic = {}
        result = []
        for i in range(len(array)):
            if tsum - array[i] in array_dic:
                result.append([tsum - array[i], array[i]])
            else:
                array_dic[array[i]] = i
        min_num = 99999999
        res = [0, 0]
        for re in result:
            if re[0] * re[1] < min_num:
                min_num = re[0] * re[1]
                res[0], res[1] = re[0], re[1]
        if res[0] + res[1] != tsum:
            return []
        res.sort()
        return res

    def FindNumbersWithSum2(self, array, tsum):
        if len(array) < 2:
            return []
        i = 0
        j = len(array) - 1
        while i < j:
            sum = array[i] + array[j]
            if sum == tsum:
                return [array[i], array[j]]
            elif sum > tsum:
                j -= 1
            else:
                i += 1
        return []


array = [1, 2, 4, 7, 11, 15]
print(Solution().FindNumbersWithSum2(array, 15))
