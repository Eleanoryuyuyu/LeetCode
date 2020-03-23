from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) < 1:
            return 0
        low = 1
        high = max(piles)
        while low < high:
            mid = (high-low)//2 + low
            if self.checkValid(mid, piles, H):
                low = mid + 1
            else:
                high = mid
        return low
    def checkValid(self, speed, piles, H):
        m = 0
        for p in piles:
            m += (p + speed - 1)//speed
        return m > H
piles = [30,11,23,4,20]
H = 6
print(Solution().minEatingSpeed(piles, H))