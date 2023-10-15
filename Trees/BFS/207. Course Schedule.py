from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        # intiailize dependencies to 0
        course_dependency = [0 for _ in range(numCourses)]
        # build dependency graph
        for edge in prerequisites:
            course_map[edge[0]].append(edge[1])
            course_dependency[edge[1]] += 1
        # initialize queue and add independent course
        queue = deque()
        for i in range(numCourses):
            if course_dependency[i] == 0:
                queue.append(i)
        # if no independent course exists return False
        if not queue:
            return False
        count = 0

        while queue:
            temp_course = queue.popleft()
            count += 1
            # iterate through all courses which are dependent on poped course
            for pre_course in course_map[temp_course]:
                # decrement dependency
                course_dependency[pre_course] -= 1
                # if all dependencies are satisfied (count is 0) add to queue
                if course_dependency[pre_course] <= 0:
                    queue.append(pre_course)
        # check if all courses are satisfied or not
        return count == numCourses
