# 690. Employee Importance
# https://leetcode.com/problems/employee-importance/

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        n_sum = 0
        for i in range(len(employees)):
            if employees[i].id != id : continue
            else : 
                n_sum += employees[i].importance
                id_list = employees[i].subordinates
            if id_list : n_sum += self.checkId(employees[i], id_list)
        return n_sum

    def checkId(self, employee_list, id_list):
        if employee_list[0] in id_list : return employee_list[1]