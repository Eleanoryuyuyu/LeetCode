class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        charSeq = {}
        for i in range(len(s)):
            if s[i] in charSeq and start <= charSeq[s[i]]:
                start = charSeq[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            charSeq[s[i]] = i
        return maxLength
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))