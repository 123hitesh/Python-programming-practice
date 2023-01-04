#write a function to calculate factorial of a number and by calling the function print the factorial from 1 to 10

def facto(a):
    f=1
    while a!=0:
        f=f*a
        a=a-1
    return f
for i in range(1,11):
    print(facto(i))


