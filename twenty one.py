# write a program to input two integers and print all the even numbers between that range
a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))
while a<=b:
    if a%2!=0:
        print(a)
    a=a+1
   
