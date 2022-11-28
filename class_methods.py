class Employee:
    company = "Natraz"
    salary = 1000
    location = "Delhi"

    # def changeSalary(self, sal):
    #     # self.salary = sal
    #     self.__class__.salary = sal
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()  
print(e.salary)

e.changeSalary(455)

print(e.salary)
print(Employee.salary)
print("ye first code hai")