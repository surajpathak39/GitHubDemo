# class Employee:
#     def __init__(self):
#         print('this is a constructor')
# suraj = Employee() 
# Employee.__init__(suraj)

class Employee:
    # name = "test"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('this is a constructor')
    # def getDetails(self):
    #     print(f'The name of the employee is {self.name}')    
    #     print(f'The name of the employee is {self.salary}')    
    #     print(f'The name of the employee is {self.subunit}')    
    def getDetails(self):
        print(f'The name of the employee is {self.name}')    
        print(f'The salary of the employee is {self.salary}')    
        print(f'The subunit of the employee is {self.subunit}')    
suraj = Employee("Suraj",2000,"Youtube") 
# suraj.name = ''
# suraj.salary = 1000
# suraj.subunit = "Google"
# suraj = Employee() 
suraj.getDetails()
