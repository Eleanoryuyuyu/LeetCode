class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 1:
            return 0
        mapping = {}
        for c in s:
            mapping[c] = mapping.setdefault(c, 0) + 1
        res = 0
        tmp = set()
        for k, v in mapping.items():
            if v % 2 == 0:
                res += v
            else:
                if v > 2:
                    res += (v-1)
                tmp.add(k)

        if len(tmp) > 0:
            res += 1
        return res
print(Solution().longestPalindrome("ccc"))
