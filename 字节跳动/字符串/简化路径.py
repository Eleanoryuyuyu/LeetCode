class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i not in ['', '.', '..']:
                stack.append(i)
            elif i == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)

print(Solution().simplifyPath("/a/./b/../../c/"))