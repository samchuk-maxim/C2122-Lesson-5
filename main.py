from contextlib import nullcontext

print("Lesson 5")

class Employee:
    def __init__(self, surname, name, age, experience):
        self.Surname = surname
        self.Name = name
        self.Age = age
        self.Experience = experience
        self.Rate = 400
        self.calculate_salary()

    def print_employee_info(self):
        print("Прізвище:", self.Surname)
        print("Імя:", self.Name)
        print("Досвід:", self.Experience)

    def calculate_salary(self):
        self.Salary = self.Experience * self.Rate + 8000

    def to_receive_a_salary(self):
        print("Ваша ЗП:", self.Salary)

emloyee1=Employee("Sigma","Oleksand",37,7)

emloyee1.print_employee_info()
emloyee1.to_receive_a_salary()


class Driver(Employee):
    def __init__(self,surname, name, age, experience,transport):
        super().__init__(surname,name,age,experience)
        self.Rate=1100
        self.calculate_salary()
        self.Transport=transport
    def show_transport(self):
        print("Транспорт:", self.Transport)

print()

emloyee2=Driver("Kogut","Oleg",27,2,"AboBus Bohdan")

emloyee2.print_employee_info()
emloyee2.show_transport()
emloyee2.to_receive_a_salary()

class Inspector(Employee):
    def __init__(self,surname, name, age, experience,license):
        super().__init__(surname,name,age,experience)
        self.Rate=1100
        self.calculate_salary()
        self.License=license
    def show_license(self):
        print("Номер ліцензії:", self.License)

print()

emloyee3=Inspector("Kogut","Oleg",27,2,"123443-123123")

emloyee3.print_employee_info()
emloyee3.show_license()
emloyee3.to_receive_a_salary()

