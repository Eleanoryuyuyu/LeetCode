from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.backtrack(s, [])
        return self.res

    def backtrack(self, s, cur):
        if len(s) == 0 and len(cur) == 4:
            self.res.append('.'.join(cur))
            return
        if len(cur) < 4:
            for i in range(min(3, len(s))):
                l, r = s[:i + 1], s[i + 1:]
                if l and 0 <= int(l) <= 255 and str(int(l)) == l:
                    self.backtrack(r, cur + [l])


print(Solution().restoreIpAddresses("25525511135"))
