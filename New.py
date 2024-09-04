class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

# Create an employee object
employee1 = Employee("John Doe", 50000)

# Get the employee's name
name = employee1.get_name()
print("Name:", name)  # Output: Name: John Doe

# Get the employee's salary
salary = employee1.get_salary()
print("Salary:", salary)  # Output: Salary: 50000

