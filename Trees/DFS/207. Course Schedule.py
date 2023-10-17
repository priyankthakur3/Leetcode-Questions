from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        visited = [0 for _ in range(numCourses)]

        def dfs_helper(course):
            # if course is being visited (dependencies not ) return False
            if visited[course] == 1:
                return False
            if visited[course] == -1:
                return True
            # course is being visited dependencies are being satisfied
            visited[course] = 1

            for dependent in course_map[course]:
                if not dfs_helper(dependent):
                    return False
            visited[course] = -1
            return True

        for edge in prerequisites:
            course_map[edge[1]].append(edge[0])

        for i in range(numCourses):
            if not dfs_helper(i):
                return False

        return True
