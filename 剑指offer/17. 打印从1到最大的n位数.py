class Solution:
    def print1ToMaxOfN(self, n):
        s = '9' * n
        for i in range(int(s) + 1):
            print(i)

Solution().print1ToMaxOfN(3)