class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        need, window = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1
        l, r = 0,  0
        valid = 0
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1
            if r - l == len(s1):
                if valid == len(need):
                    return True
                c = s2[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
