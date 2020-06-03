class Solution:
    def sumNums(self, n: int) -> int:
        return n != 0 and n + self.sumNums(n-1)

print(Solution().sumNums(9))