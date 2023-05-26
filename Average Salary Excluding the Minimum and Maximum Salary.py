class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        maximum_salary = 0
        minimum_salary = sys.maxsize
        number_of_employee = 0

        for payment in salary:
            total += payment
            maximum_salary = max(maximum_salary, payment)
            minimum_salary = min(minimum_salary, payment)
            number_of_employee += 1

        res = (total - maximum_salary - minimum_salary) / (number_of_employee - 2)
        return res