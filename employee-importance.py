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
        Graph={}
        importance={}
        for employee in employees:
            if employee.id in Graph:
                Graph[employee.id].extend(employee.subordinates)
            else:
                Graph[employee.id]=employee.subordinates
            importance[employee.id]=employee.importance
        queue=[id]
        res=importance[id]
        visite=set()
        visite.add(id)
        while queue:
            vertex = queue.pop()
            for adjvertex in Graph[vertex]:
                if adjvertex not in visite:
                    res+=importance[adjvertex]
                    queue.append(adjvertex)
                    visite.add(adjvertex)
        return res