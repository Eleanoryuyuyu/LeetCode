class Solution:
    def FindNumberAppearingOnce(self, array):
        if len(array) < 1:
            return
        bitArr = [0]*32
        for i in array:
            flag = 1
            for j in range(31, -1, -1):
                if i & flag != 0:
                    bitArr[j] += 1
                flag = flag << 1
        result = 0
        for i in range(32):
            result = result << 1
            result += bitArr[i] % 3
        return result

array =  [2,3,2,4,2,3,3]
print(Solution().FindNumberAppearingOnce(array))