# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        ss = list(ss)
        res = []
        self.PermutationHelper(ss, 0, res)
        res.sort()
        return res

    def PermutationHelper(self, ss, begin, res):
        if begin == len(ss):
            new_str = "".join(ss)
            if new_str not in res:
                res.append("".join(ss))
        else:
            for i in range(begin, len(ss)):
                ss[begin], ss[i] = ss[i], ss[begin]
                self.PermutationHelper(ss, begin + 1, res)
                ss[begin], ss[i] = ss[i], ss[begin]
    # 字符的全排列组合
    def Permutation2(self, ss):
        if not ss:
            return []
        ss = list(ss)
        res = [""]
        for w in ss:
            res += [c + w for c in res]
        return res




print(Solution().Permutation2("abc"))
