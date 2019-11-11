class Solution:
    def majorityElement(self, nums):
        c = t = 0
        for num in nums:
            if c == num:
                t += 1
            elif c == 0:
                c = num
                t = 1
            else:
                t -= 1
        return c