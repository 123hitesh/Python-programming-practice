#program to accept electricity units
bill=eval(input("Enter the number of electricity units: "))
if bill<=100:
    a=bill*0
    print("The rates for these units is FREE")
elif bill>100 and bill<300:
    b=(bill-100)*2
    print("The total bill is ",b)
else:
    c=(bill-300)*5+400
    print("The total bill is",c)
