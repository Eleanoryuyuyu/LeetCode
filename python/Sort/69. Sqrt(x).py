class Solution:
    def mySqrt(self, x):
        if x <= 0:
            return 0
        if x == 1:
            return 1
        low = 1
        high = x // 2 + 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return int(mid)
        return (low+high)//2
s = Solution()
print(s.mySqrt(16))
