class Solution:
    def longestSubstringWithoutDup(self, s):
        if len(s) < 1:
            return 0
        maxLen = 0
        str_map = {}
        start = 0
        for i in range(len(s)):
            if s[i] in str_map and start <= str_map[s[i]]:
                start = str_map[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            str_map[s[i]] = i
        return maxLen

print(Solution().longestSubstringWithoutDup("arabcacfr"))
