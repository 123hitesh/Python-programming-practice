# write a program to input 2 variables a and b and take input of the
#operation to be performed

a=eval(input ("enter the first number: "))
b=eval(input("Enter the second number:" ))
op=input("Enter the operation to be performed: ")
if op=="+":
       print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("Invalid operator added")
