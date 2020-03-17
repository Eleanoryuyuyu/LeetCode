from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if len(words) < 1 or len(chars) < 1:
            return 0
        char_dic = Counter(chars)
        res = 0
        for w in words:
            tmp = Counter(w)
            for c in tmp:
                if c not in char_dic or tmp[c] > char_dic[c]:
                    break
            else:
                res += len(w)

        return res

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(Solution().countCharacters(words, chars))

