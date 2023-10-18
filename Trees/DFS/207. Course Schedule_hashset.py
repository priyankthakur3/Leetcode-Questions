from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build pre requite list
        course_map = defaultdict(list)

        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        # visited nodes list
        visited = set()

        def dfs_helper(course):

            #  course already visited
            if course in visited:
                return False
            # if there are no pre-requites
            if len(course_map[course]) == 0:
                return True
            # add to visiting set
            visited.add(course)

            for prereq in course_map[course]:

                if not dfs_helper(prereq):
                    return False

            # already done visiting nodes pop from hashSet
            visited.remove(course)
            # all nodes are visited remove dependency
            course_map[course] = []
            return True

        # run dfs on all courses
        for course in range(numCourses):
            if not dfs_helper(course):
                return False

        return True
