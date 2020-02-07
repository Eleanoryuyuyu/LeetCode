class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n != 0 and n & (n - 1) == 0:
            return True
        return False


print(Solution().isPowerOfTwo(6))
