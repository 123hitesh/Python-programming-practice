'''#create a class using attributes
class student:
    roll_no=0
    name=None
    def print_details(self):
        roll_no=int(input("Enter roll number: "))
        name=input("Enter name: ")
        print(roll_no,name)

s1=student()
s1.print_details()'''


    

'''class student:
    def get_details(self,r,n):
        self.r=r
        self.n=n
    def print_details(self):
        print(self.r,self.n)

s1=student()
s1.get_details(1,"Rohit Kumar")
s1.print_details()

s2=student()
r=int(input("Roll No: "))
n=input("Enter name: ")
s2.get_details(r,n)
s2.print_details()'''




'''#create class without using attributes
class students():
    def get_details(self,r,n):
        self.r=r
        self.n=n
    def print_details(self):
        print(self.r,self.n)
s1=student()
s1.get_details(1,"Rohit Kumar")
s1.print_details()




# class with in it method'''
'''class Student():
    def__init__(self,r,n):
        self.r=r
        self.n=n
        print(self.r,self.n)
    s1=student(1,"Rohit")'''




'''class Employee():
    pass
Emp1=Employee()
name=input("name: ")
Emp1.name=name
Emp1.age=25
Emp1.salary=25000
print("Emp1.name: ",Emp1.name)
print("Emp1.salary: ",Emp1.salary)'''






