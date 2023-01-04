#program to find the reverse of a number using while loop
n=eval(input("Enter the number whose reverse you wants: "))
rev=0
while n!=0:
    t=n%10
    rev=rev*10+t
    n=n//10
print("Reverse of number is",rev)
