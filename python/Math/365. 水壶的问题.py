class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:
            return True
        if x + y < z:
            return False
        if x > y:
            x, y = y, x
        if x == 0:
            return y == z
        while y % x != 0:
            y, x = x, y%x
        return z % x == 0

print(Solution().canMeasureWater(2,6,5))