class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        flag = 1
        res = 0
        x = 10
        for i in range(len(str)):
            if i == 0:
                if str[i] == '-':
                    flag = -1
                elif str[i] == '+':
                    flag = 1
                elif ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
                    res = int(str[i])
                else:
                    return 0
            elif i > 0 and ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
                if res == 0:
                    x = 1
                res = res * x + int(str[i])
                x = 10
            else:
                break
        res = res * flag
        if res > 2 ** 31 -1:
            return 2 ** 31 - 1
        if res < -2**31:
            return -2**31
        return res

print(Solution().myAtoi("-91283472332"))

