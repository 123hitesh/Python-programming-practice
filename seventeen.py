#write a program to check whether a three digit number is armstrong number or not
n=eval(input("Enter the number to check: "))
x=n
s=0
while n!=0:
    t=n%10
    s=s+t**3
    n=n//10
if s==x:
    print("The given Number is Armstrong")
else:
    print("The given Number is not Armstrong")
