class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split(" ")
        s_list = [c for c in s_list if c != ""]
        res = " ".join(s_list[::-1])
        return res


s = "a good   example"
print(Solution().reverseWords(s))
