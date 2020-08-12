"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        def getSum(dic, D_list, s = 0): 
            for n in D_list : 
                s += dic[n][0]
                if dic[n][1] : s += getSum(dic,dic[n][1])
            return s
        
        dic, n_sum = {}, 0
        for employee in employees:
            dic[employee.id] = [employee.importance, employee.subordinates]
        
        n_sum += dic[id][0]
            
        for sub in dic[id][1]:
            n_sum += dic[sub][0]
            if dic[sub][1] : 
                n_sum += getSum(dic, dic[sub][1])
        
        return n_sum

"""
# n_sum 선언 x, 바로 처음 importance에 더해버림
        dic = {}
        for employee in employees:
            dic[employee.id] = [employee.importance, employee.subordinates]
            
        dic[id][0] += getSum(dic, dic[id][1])
        
        return dic[id][0]
"""