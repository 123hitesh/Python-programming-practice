#write a program202 t220o check whether a year is leap year
a=eval(input("enter the year: "))
if (a%100==0 and a%400==0):
    print("the year is a leap year")
elif (a%4==0 and a%100!=0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")
