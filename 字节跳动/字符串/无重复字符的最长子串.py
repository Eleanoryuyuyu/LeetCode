class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        mapping = {}
        res = 1
        mapping[s[0]] = 0
        start = 0
        for i in range(1, len(s)):
            if s[i] in mapping and start <= mapping[s[i]]:
                start = mapping[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            mapping[s[i]] = i
        return res
s = "tmmzuxt"
print(Solution().lengthOfLongestSubstring(s))
