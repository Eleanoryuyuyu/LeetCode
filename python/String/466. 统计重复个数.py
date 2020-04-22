class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not s1 or not s2:
            return 0
        repeatCnt = [0] * (n1+1)
        nextIndex = [0] * (n1+1)
        j, cnt = 0, 0
        for k in range(1, n1+1):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                if j == len(s2):
                    j = 0
                    cnt += 1
            repeatCnt[k] = cnt
            nextIndex[k] = j
            for start in range(k):
                if nextIndex[start] == j:
                    interval = k - start
                    repeat = (n1-start)//interval
                    patternCnt = (repeatCnt[k] - repeatCnt[start]) * repeat
                    remainCnt = repeatCnt[start + (n1-start) % interval]
                    return (patternCnt + remainCnt) // n2
        return repeatCnt[n1] // n2

s1 ="aaa"
n1 = 3
s2 ="aa"
n2 = 1
print(Solution().getMaxRepetitions(s1, n1, s2, n2))