class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def total_salary(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        return total




emp1 = Employee("Петро", "Менеджер", 1500)
emp2 = Employee("Степан", "Начальник", 1834)

department = Department()

department.add_employee(emp1)
department.add_employee(emp2)

department.remove_employee(emp1)

print(department.total_salary())
