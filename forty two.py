def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a//b
while True:
    ch=input("Press + for addition ,Press -for subtraction,Press *for multiply,Press//for div,Press # for exit")
    if ch=="+":
        a,b=eval(input("Enter the values of a and b "))
        print("Sum of numbers is: ",add(a,b))
    elif ch=="-":
        a,b=eval(input("Enter the values of a and b "))
        print("Difference of numbers is: ",sub(a,b))
    elif ch=="*":
        a,b=eval(input("Enter the values of a and b "))
        print("Product of numbers is: ",multiply(a,b))
    elif ch=="/":
        a,b=eval(input("Enter the values of a and b "))
        print("Division of numbers is: ",division(a,b))
    elif ch=="#":
        break 
    else:
        print("Invalid Operation entered")
print("Thankyou for using Mini calculator")
    
