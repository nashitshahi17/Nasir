# Write a method salaryafterincrement method with @property decorator setter which changes the value of increment based on salary
class Sal:
    salary = 550
    increment = 20
    @property
    def val(self):
        return (self.salary + self.salary *(self.increment/100))

a = Sal()
print(a.val)