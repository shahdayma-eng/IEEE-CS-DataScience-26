class Employee:

    def __init__(self, n, s):
        self.n = n
        self.s = s

    def get_annual_salary(self):
        return self.s * 12

    def display_info(self):
        print("----- Employee Info -----")
        print("Name:", self.n)
        print("Monthly Salary:", self.s)
        print("Annual Salary:", self.get_annual_salary())
        print("-------------------------")


n = input("Enter name: ")
s = float(input("Enter monthly salary: "))

e = Employee(n, s)
e.display_info()