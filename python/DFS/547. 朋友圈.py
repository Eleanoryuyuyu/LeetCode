from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M) < 1 or len(M[0]) < 1:
            return 0
        res = 0
        visited = [0] * len(M)
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, i, visited)
                res += 1
        return res

    def dfs(self, M, i, visited):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, j, visited)

M = [[1,1,0],
 [1,1,1],
 [0,1,1]]
print(Solution().findCircleNum(M))