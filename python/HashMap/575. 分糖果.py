from typing import List
import sys

class Solution:
    # 暴力, 时间复杂度O(n**2)，空间复杂度O(1)
    def distributeCandies1(self, candies: List[int]) -> int:
        if len(candies) < 1:
            return 0
        count = 0
        i = 0
        n = len(candies)
        while i < n and count < n//2:
            if candies[i] != -(sys.maxsize-1):
                count += 1
                for j in range(i+1, n):
                    if candies[j] == candies[i]:
                        candies[j] = -(sys.maxsize-1)
            i += 1
        return count

    # 排序， 时间复杂度O(nlogn)， 空间复杂度O(1)
    def distributeCandies2(self, candies: List[int]) -> int:
        n = len(candies)
        if n < 1:
            return 0
        candies.sort()
        count = 1
        i = 1
        while i < n and count < n//2:
            if candies[i] > candies[i-1]:
                count += 1
            i += 1
        return count
    #集合， 时间复杂度O(n)， 空间复杂度O(n)
    def distributeCandies3(self, candies: List[int]) -> int:
        n = len(candies)
        if n < 1:
            return 0
        can_set = set(candies)
        return min(len(can_set), n//2)


candies = [1,1,2,2,3,3]
print(Solution().distributeCandies3(candies))
