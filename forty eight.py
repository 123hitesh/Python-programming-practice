#write a function to count number of digits in a number

def num_count(a):
    count=0
    while a!=0:
        count=count+1
        a=a//10

a=int(input("Enter a number: "))
print("The number",a,"has digits",num_count(a))
