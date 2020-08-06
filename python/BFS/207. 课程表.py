from typing import List


class Solution:
    # BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        post_courses = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        queue = []
        for (cur, pre) in prerequisites:
            post_courses[cur] += 1
            adj[pre].append(cur)
        for i in range(numCourses):
            if post_courses[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adj[pre]:
                post_courses[cur] -= 1
                if post_courses[cur] == 0:
                    queue.append(cur)
        return True if numCourses == 0 else False
    #dfs
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adj[i]:
                if not dfs(j):
                    return False
            flags[i] = -1
            return True
        flags = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



numCourses = 2
prerequisites = [[1,0],[0,1]]
print(Solution().canFinish2(numCourses, prerequisites))