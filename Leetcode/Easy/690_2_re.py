"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# stack 사용 DFS
# 내가 짠 코드 아님
class Solution:
    def getImportance(self, employees, id):
        id_to_emp = {employee.id: employee for employee in employees}
        importance = 0
        stack = [id_to_emp[id]]
        while stack:
            cur_emp = stack.pop()
            importance += cur_emp.importance
            stack.extend([id_to_emp[new_emp] for new_emp in cur_emp.subordinates])
        return importance 