class Solution:
    # 1. 哈希表
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        elif (not s or not t) or (len(s) != len(t)):
            return False
        mapa = {}
        mapb = {}
        for i in s:
            mapa[i] = mapa.get(i, 0) + 1
        for i in t:
            mapb[i] = mapb.get(i, 0) + 1
        return mapa == mapb

    # 2. 排序，时间复杂度O(nlogn)
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "rat"
t = "car"
print(Solution().isAnagram2(s, t))
