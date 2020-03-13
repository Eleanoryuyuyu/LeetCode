from math import gcd


class Solution:
    # 1. 枚举
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1%i == 0 and len2 % i ==0:
                if str1[:i] * (len1//i) == str1 and str1[:i] * (len2//i) == str2:
                    return str1[:i]
        return ""

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        cand_len = gcd(len1, len2)
        if str1[:cand_len] * (len1//cand_len) == str1 and str1[:cand_len] * (len2//cand_len) == str2:
            return str1[:cand_len]
        return ""
    def gcdOfStrings3(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        cand_len = gcd(len1, len2)
        candidate = str1[:cand_len]
        if str1 + str2 == str2 + str1:
            return candidate
        return ""

str1 = "ABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings3(str1, str2))