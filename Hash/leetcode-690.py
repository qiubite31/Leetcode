"""
690. Employee Importance
Difficulty: Easy
Related Topic: Hash, Breadth-first Search

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp_dict = {emp.id: emp for emp in employees}

        total_score = 0
        emp_queue = [emp_dict[id]]
        while emp_queue:
            emp = emp_queue.pop(0)

            total_score += emp.importance
            for emp_id in emp.subordinates:
                emp_queue.append(emp_dict[emp_id])

        return total_score

employee2 = Employee(2, 3, [4])
employee3 = Employee(3, 4, [])
employee1 = Employee(1, 5, [2, 3])
employee4 = Employee(4, 1, [])

employees = [employee1, employee2, employee3, employee4]
id = 1
solution = Solution()
output = solution.getImportance(employees, id)

print(output)
