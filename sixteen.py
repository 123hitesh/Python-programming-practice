#write a program to input a number and check whether that number is a palindrome number or not
n=eval(input("Enter the Number: "))
rev=0
x=n
while n!=0:
    t=n%10
    rev=rev*10+t
    n=n//10
if x==rev:
    print("number is palindrome")
else:
    print("Number is not palindrome")
