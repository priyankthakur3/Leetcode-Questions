class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {x: [] for x in range(numCourses)}
        for c, p in prerequisites:
            course_map[c].append(p)
        result = []
        visited, cycle = set(), set()

        def dfs_helper(course):
            # course will have 3 states
            # visited: course has been visited
            # visiting: course has been added to cycle but not visited or result
            # unvisited: course has not added to cycle or visited

            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in course_map[course]:
                if not dfs_helper(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
        
        for crs in range(numCourses):
            if not dfs_helper(crs):
                return []
        
        return result