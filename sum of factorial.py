import math
a=int(input())
b=int(input())
sum=0
for i in range(a,b+1):
    sum=sum+math.factorial(i)
print(sum)
