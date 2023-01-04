# program to input a number and print all the numbers from 1 to n which are
# divsible by 3 as well as 5

n=eval(input("Enter the number :"))
i=1
while i<=n:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1
