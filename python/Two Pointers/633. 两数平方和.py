class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(c ** 0.5)
        while i <= j:
            sum = i**2 + j**2
            if sum < c:
                i += 1
            elif sum > c:
                j -= 1
            else:
                return True
        return False
print(Solution().judgeSquareSum(1))
