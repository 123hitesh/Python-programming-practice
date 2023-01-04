#function to count the number of digits in a numberand according to
#number of digits check whether the number is armstrong number or not

def count(n):
    count=0
    while n!=0:
        count=count+1
        n=n//10   
    return count
x=n
s=0
while n!=0:
    t=n%10
    s=s+t**count
    n=n//10
    if s==x:
return True
    else:
return False
