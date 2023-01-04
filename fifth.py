# a company decided to give bonus according to following criteria
sal=eval(input("Enter your salary: "))
exp=eval(input("Enter the number of years of experience: "))
if exp>10:
    print("the yearly bonus is",15/100*sal)
elif exp>6 and exp<10:
     print("the yearly bonus is",10/100*sal)
else:
     print("the yearly bonus is",5/100*sal)
