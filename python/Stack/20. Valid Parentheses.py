class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif stack and s[i] in [')', ']', '}']:
                tmp = stack.pop()
                if tmp + s[i] not in ['()', '[]', '{}']:
                    return False
            else:
                return False
        if stack:
            return False
        return True

    def isValid2(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in range(len(s)):
            if s[i] in dic:
                stack.append(s[i])
            elif stack:
                tmp = stack.pop()
                if s[i] != dic[tmp]:
                    return False
            else:
                return False
        if stack:
            return False
        return True

    def isValid3(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            elif stack and s[i] != stack.pop():
                return False
            else:
                return False
        if stack:
            return False
        return True



s = Solution()
print(s.isValid3("(()"))
