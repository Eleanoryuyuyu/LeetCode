from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        post_courses = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        queue = []
        res = []
        for cur, pre in prerequisites:
            post_courses[cur] += 1
            adj[pre].append(cur)
        for i in range(numCourses):
            if post_courses[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            numCourses -= 1
            for cur in adj[pre]:
                post_courses[cur] -= 1
                if post_courses[cur] == 0:
                    queue.append(cur)
        return res if numCourses == 0 else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))