class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

    def hammingWeight2(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        mask = 1
        for _ in range(32):
            if n&mask:
                count += 1
            mask = mask << 1
        return count


print(Solution().hammingWeight2(5))
