"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {}
        # build employee hashmap
        for employee in employees:
            employee_map[employee.id] = employee
        importance = 0
        # add id to queue
        queue = deque([id])

        while queue:
            employee_id = queue.popleft()
            # increment importance
            importance += employee_map[employee_id].importance
            # iterate through all subordinate and add them to queue
            for subordinate in employee_map[employee_id].subordinates:
                queue.append(subordinate)

        return importance
