from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: [-len(x), x])
        for target in d:
            if self.isValid(s,target):
                longestStr = target
                return longestStr
        return ""
    def isValid(self,s,target):
        i, j = 0, 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j += 1
            i += 1
        return j == len(target)

s = "abpcplea"
d = ["a","b","c"]
print(Solution().findLongestWord(s, d))