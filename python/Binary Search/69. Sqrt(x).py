class Solution:
    def mySqrt(self, x):
        if x <= 0:
            return 0
        if x == 1:
            return 1
        low = 1
        high = x//2 + 1
        while low <= high and (high - low) > 1e-2:
            mid = (low + high) / 2
            if mid * mid > x:
                high = mid  # 因为是浮点型，所以不能加1
            elif mid * mid < x:
                low = mid
            else:
                return mid
        return (low+high)/2
s = Solution()
print(s.mySqrt(2))
