class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)

    def myPow2(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            x = 1.0 / x
            n = -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


print(Solution().myPow2(2, 2))
