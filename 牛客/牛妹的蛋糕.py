class Solution:
    def cakeNumber(self, n ):
        remain = 1
        for _ in range(n-1):
            remain = (remain + 1)*3//2

        return int(remain)
print(Solution().cakeNumber(4))