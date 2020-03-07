from typing import List


class Solution:
    # 暴力
    def distributeCandies1(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        if candies < 1:
            return res
        i = 0
        while candies != 0:
            res[i % num_people] += min(i+1, candies)
            candies -= min(i+1, candies)
            i += 1
        return res
    # 数学
    def distributeCandies2(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        if candies < 1:
            return res
        """
        1. 完整分发的糖果的构成一个等差数列：1+2+……+p = 1/2*p*(p+1)
           其中 0 < 1/2*p*(p+1) < candies, 求得 p = floor(sqrt(2c + 1/4)-1/2)
           remain = candies - p*(p+1)*1/2
        2. 完整分发轮次 row = p//num, 最后剩下获得剩余糖果的人 col = p%num
        3. 在完整分发轮次，每人获得的糖果为 res[i] += (i+1)*row + n*row*(row-1)*1/2
           最后一个回合不完整，在col之前的人能再获得一次 i+1+n*row, 在col上的人获得remain。
        """
        p = int((2*candies + 0.25)**0.5 - 0.5)
        remain = candies - int(0.5*p*(p+1))
        rows = p // num_people
        col = p % num_people
        for i in range(num_people):
            res[i] = (i+1)*rows + num_people*int(rows*(rows-1)*0.5)
            if i < col:
                res[i] += (i+1)+num_people*rows
        res[col] += remain
        return res

print(Solution().distributeCandies1(10,3))