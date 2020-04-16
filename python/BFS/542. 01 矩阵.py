from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) < 1:
            return matrix
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        queue = [(i,j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        visited = set(queue)
        while queue:
            curi, curj = queue.pop(0)
            for ni, nj in [(curi - 1, curj), (curi + 1, curj), (curi, curj - 1), (curi, curj + 1)]:
                if 0<=ni<m and 0<=nj<n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[curi][curj] + 1
                    queue.append((ni, nj))
                    visited.add((ni, nj))
        return dist



matrix = [[0],[0],[0],[0],[0]]
print(Solution().updateMatrix(matrix))