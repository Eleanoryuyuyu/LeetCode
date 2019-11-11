class Solution:
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for cur in dict[digits[num]]:
                dfs(num + 1, string + cur, res)

        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        length = len(digits)
        if length == 0:
            return []
        res = []
        dfs(0, "", res)
        return res

    def letterCombinations2(self, digits):
        if digits == "":
            return []
        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        res = [""]
        for cur in digits:
            res = [w + c for c in dict[cur] for w in res]
        return res


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations2("23"))