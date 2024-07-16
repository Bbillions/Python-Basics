data1 = {
    'Name':"Adams",
    'ID':'E7876',
    'SALARY':50000,
    'DEPARTMENT':'ACCOUNTING'
}
data2 = {
    'Name':"Jones",
    'ID':'E7499',
    'SALARY':45000,
    'DEPARTMENT':'RESEARCH'
}
data3 = {
    'Name':"Martin",
    'ID':'E7900',
    'SALARY':50000,
    'DEPARTMENT':'SALES'
}
data4 = {
    'Name':"Smith",
    'ID':'E7698',
    'SALARY':55000,
    'DEPARTMENT':'OPERATIONS'
}
"""class employ
1.use assign department to change the department of an employee
2. calculate overtime salary... use 'calculate_emp_salary' method takes two arguments: salary and hours worked,
which is the number of hour worked by the employee.
if the number of hours worked is more than 50, the method computes overtime and add it to the salary, overtime formula

overtime = hours_worked - 50
overtime_amount = overtime * (salary/50)

3. write a function that adds all the salary of employees together and returns the mean
"""


# Solution in class
class Employee():
    def __init__(self,Name, ID, Salary, Department):
        self.Name = Name
        self.ID = ID
        self.Salary = Salary
        self.Department = Department

    def Outputdetails(self):
        print(F'{self.Name} {self.ID} {self.Salary} {self.Department}')

    def assign_department(self,new_department):
        self.Department = new_department
        return self.Department
    
    def calculate_emp_salary(self, hours_worked):
        overtime = hours_worked - 50
        overtime_amount = overtime*(self.Salary/50)

        return overtime_amount+self.Salary
    
    
emp1 =  Employee('Smith','E7698', 55000,'OPERATIONS')
emp2 = Employee("Adams",'E7876',50000,'ACCOUNTING')
emp3 = Employee("Jones",'E7499',45000,'RESEARCH')
emp4 = Employee("Martin",'E7900',50000,'SALES')

h_w = [55,63,78,60]
emp_list = [emp1,emp2,emp3,emp4]
print(emp1.name)
print(emp1.Department)
print(emp1.assign_department('Technical'))
print(emp1.Department)
print(emp1.calculate_emp_salary(82))

def calculate_all_emp_salary(list_of_emp_data):
    
    all_salary = 0

    for eachemp in list_of_emp_data:
        all_salary += eachemp.calculate_emp_salary(55)

    print(all_salary)

calculate_all_emp_salary(emp_list)


# calculate with different overtime for them
# calculate with different overtime for them
def calculate_all_emp_salary2(list_of_emp_data,hours_worked):
    
    all_salary = 0

    for eachemp in list_of_emp_data:
        pos = list_of_emp_data.index(eachemp)
        # print(eachemp.Name)
        # print(h_w[pos])

        all_salary += eachemp.calculate_emp_salary(hours_worked[pos])

    print(f'The mean  of {all_salary} = {all_salary/len(list_of_emp_data)}')

calculate_all_emp_salary2(emp_list,h_w)

