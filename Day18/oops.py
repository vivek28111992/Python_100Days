"""
Monthly Salary Settlement System-Department Manager 15000 per month Programmer 200 sales per hour 1800 base salary plus sales 5% commission
"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
  """Employee Abstract Class"""
  def __init__(self, name):
    self.name = name

  @abstractmethod
  def get_salary(self):
    """settlement monthly salary (abstract method)"""
    pass

class Manager(Employee):
  """Department Manager"""
  def get_salary(self):
    return 15000

class Programmer(Employee):
  """Programmer"""
  def __init__(self, name, working_hour=0):
    self.working_hour = working_hour
    super().__init__(name)

  def get_salary(self):
    return 200 * self.working_hour

class Salesman(Employee):
  """Salesman"""
  def __init__(self, name, sales=0.0):
    self.sales = sales
    super().__init__(name)

  def get_salary(self):
    return 1800 + self.sales * 0.05

class EmployeeFactory:
  """Create a factory for employees (factory mode-decoupling) between object consumers and objects through the factory)"""

  @staticmethod
  def create(emp_type, *args, **kwargs):
    """Create Employees"""
    all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
    cls = all_emp_types[emp_type.upper()]
    return cls(*args, **kwargs) if cls else None

def main():
  """Main function"""
  emps = [
    EmployeeFactory.create('M', 'Cao Cao'),
    EmployeeFactory.create('P', 'Xunyu', 120),
    EmployeeFactory.create('P', 'Guo Jia', 85),
    EmployeeFactory.create('S', 'Dian Wei', 123000),
  ]

  for emp in emps:
    print(f' {emp.name} : {emp.get_salary() }')

if __name__ == '__main__':
    main()
