class emp():
    def __init__(self,id,name,sal):
         self.id=id
         self.name=name
         self.salary=sal
    def inhand(self):
        self.inhandsalary=int(self.salary*0.8)


emp1=emp(101,'Ravi',20000)
emp2=emp(103,'Raj',30000)

emp1.bonace=5000

emp1.inhand()
emp2.inhand()

print(emp1.__dict__)
print(emp2.__dict__)

class maneger(emp):
    pass

man=maneger(105,'kumar',60000)
man.inhand()
print(man.__dict__)