import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dic = collections.Counter(t)
        required = len(dic)
        l, r = 0, 0
        formed = 0
        windowCounts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            windowCounts[character] = windowCounts.get(character, 0) + 1
            if character in dic and windowCounts[character] == dic[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                windowCounts[character] -= 1
                if character in dic and windowCounts[character] < dic[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

