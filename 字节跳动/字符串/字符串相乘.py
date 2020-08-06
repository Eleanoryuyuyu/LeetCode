class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tmp1, tmp2 = int(num1), int(num2)
        if tmp1 == 1:
            return num2
        if tmp2 == 1:
            return num1
        res = 0
        pos = 1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            tmp1, tmp2 = tmp2, tmp1
        for i in num2[::-1]:
            res += tmp1 * int(i) * pos
            pos *= 10
        return str(res)

num1 = '123'
num2 = '456'
print(Solution().multiply(num1, num2))