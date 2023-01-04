#write a program to print first n terms of fibonnaci series
n=eval(input("Enter the value of n: "))
t1=0
t2=1
i=3
print(t1,t2,end=" ")
while i<=n:
    ans=t1+t2
    print(ans,end=" ")
    t1=t2
    t2=ans
    i=i+1
