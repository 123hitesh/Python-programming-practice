'''class book:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def show(self):
        print(self.id,self.name,self.price)

b1=book(101,'Python',250)
b1.show()'''

#inheritance

'''class student:
    def get_info(self):
        self.reg=input("enter reg no.: ")
        self.name=input("Enter name: ")
    def show_info(self):
        print(self.reg,self.name)

class result(student):
    def get_result(self):
        self.marks=int(input("Enter marks: "))
    def show_marks(self):
        print(self.marks)

r=result()
r.get_info()
r.show_info()
r.get_result()
r.show_marks()'''

#multiple inheritance
'''class employee:
    def get_info(self):
        self.id=input("enter employee id: ")
        self.name=input("Enter name: ")
    def show_info(self):
        print(self.id,self.name)

class salary:
    def get_acc(self):
        self.sal=eval(input("Enter salary: "))
        self.ben=eval(input("Enter benefit: "))
    def show_acc(self):
        print(self.sal+self.ben)

class calculate(employee,salary):
    pass

c=calculate()
c.get_info()
c.show_info()
c.get_acc()
c.show_acc()'''


'''class A:
    def __init__(self):
        print("inparent class" )

class B(A):
    def __init__(self):
        super().__init__()
        print("inchild class" )

ob=B()'''


#method overloading

'''class student:
    def get_info(self,reg=None,name=None):
        self.reg=reg
        self.name=name
        print(self.reg,self.name)

s=student()
s.get_info()
s.get_info("12121212")
s.get_info("12121212","abcdef")'''

'''#private attributes and private method

class student:
    reg=" "
#private attributes
    __reg=" "
    __name=" "

    #private methods
    def __get_info(self,r,n):
        self.__reg=r
        self.__name=n

        #public methods
    def show_info(self,r,n):
        self.__get_info(r,n)
        print(self.__reg,self.__name)

s=student()
s.show_info("12121212","abc")'''


