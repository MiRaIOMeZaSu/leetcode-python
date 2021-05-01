from typing import List

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 图?
        # 动态规划?
        # 哈希表!
        # 遍历!
        # count_dict = {}
        self.id_dict = {}
        # 得到的是一个包含多个Employee的列表
        for employee in employees:
            self.id_dict[employee.id] = employee
        return self.solve(id)

    def solve(self, id):
        employee = self.id_dict[id]
        ret = employee.importance
        for subId in employee.subordinates:
            ret += self.solve(subId)
        return ret
