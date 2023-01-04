#function to calculate simple interest without passing arguement
"""def SI():
    a=eval(input("enter the principle amount: "))
    b=eval(input("enter the rate: "))
    c=eval(input("enter years: "))
    s=(a*b*c)/100
    print(s)
SI()
SI()
SI()"""
def SI(a,b,c):
    s=(a*b*c)/100
    print(s)
SI(5000,6,4)
