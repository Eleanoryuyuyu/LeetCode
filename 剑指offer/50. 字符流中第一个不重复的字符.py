# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.string = []
        self.char_dic = {}
    def FirstAppearingOnce(self):
        # write code here
        for c in self.string:
            if self.char_dic[c] == 1:
                return c
    def Insert(self, char):
        # write code here
        self.string.append(char)
        if char not in self.char_dic:
            self.char_dic[char] = 1
        else:
            self.char_dic[char] += 1
s = Solution()
s.Insert('g')
s.Insert('o')
print(s.FirstAppearingOnce())
s.Insert('o')
s.Insert('g')
s.Insert('l')
s.Insert('e')
print(s.FirstAppearingOnce())