from employee import Employee

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')

from department import Department

Department("dept1", [emp_1, emp_2])


# Logger share state between all modules under the same process

# One employees creation will be logged
# The logging in Department class will fail because department class logger[root logger]
# was already configured in Employee class
# Department class logger can override initial root logger configuration


# python root_logger_issue/main.py
