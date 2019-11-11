from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.Palindrome = lambda s: s == s[::-1]
        res = []
        self.helper(s, res, [])
        return res

    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.Palindrome(s[:i]):
                self.helper(s[i:], res, path + [s[:i]])

t = Solution()
print(t.partition("aab"))