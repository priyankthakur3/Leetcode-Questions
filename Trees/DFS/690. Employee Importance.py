"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {}
        # build hashmap for employee
        for employee in employees:
            employee_map[employee.id] = employee

        def helper(id):
            result = employee_map[id].importance
            # iterate through all subordinates to get their importance
            for subordinate in employee_map[id].subordinates:
                result += helper(subordinate)
            return result
        # start dfs
        return helper(id)
