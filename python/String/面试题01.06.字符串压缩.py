class Solution:
    def compressString(self, S: str) -> str:
        if len(S) <= 1:
            return S
        str_map = {}
        str_map[S[0]] = 1
        res = ""
        for i in range(1,len(S)):
            if i == len(S)-1:
                if S[i] not in str_map:
                    res += S[i-1] + str(str_map[S[i-1]]) + S[i] + str(1)
                else:
                    res += S[i] + str(str_map[S[i]] + 1)
            elif S[i] == S[i-1]:
                str_map[S[i]] += 1
            else:
                res += S[i-1] + str(str_map[S[i-1]])
                str_map = {}
                str_map[S[i]] = 1
        if len(res) >= len(S):
            return S
        else:
            return res

   # 官方题解， 简洁版
    def compressString2(self, S: str) -> str:
        if not S:
            return ""
        ch = S[0]
        ans = ''
        cnt = 0
        for c in S:
            if c == ch:
                cnt += 1
            else:
                ans += ch + str(cnt)
                ch = c
                cnt = 1
        ans += ch + str(cnt)
        return ans if len(ans) < len(S) else S




print(Solution().compressString("bbbac"))