from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        mapping = {}
        res = ""
        lens = [len(x) for x in strs]
        l = min(lens)
        for i in range(l):
            mapping[i] = set()
            for s in strs:
                mapping[i].add(s[i])
            if len(mapping[i]) > 1:
                break
            if len(mapping[i]) == 1:
                res += list(mapping[i])[0]
        return res
strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))

