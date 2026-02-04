class Employee:
    def __init__(self, empid, empname, designation, basic_salary, exp):
        self.empid = empid
        self.empname = empname
        self.designation = designation
        self.basic_salary = basic_salary
        self.exp = exp

    def display_details(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Designation:", self.designation)
        print("Basic Salary:", self.basic_salary)
        print("Experience (years):", self.exp)

    def calculate_salary(self):
        if self.exp > 10:
            allowance = 0.20 * self.basic_salary
        elif 10>= self.exp >=5:
            allowance = 0.10 * self.basic_salary
        else:
            allowance = 0.05 * self.basic_salary

        print("Allowance:", allowance)
        print("Total Salary:", self.basic_salary + allowance)

empobj = Employee(101, "John Doe", "Software Engineer", 50000, 7)
empobj.display_details()
empobj.calculate_salary()

