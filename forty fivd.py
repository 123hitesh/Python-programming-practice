#function to calculate Simple Interest using lambda expression

SI= lambda p,r,t : (p*r*t)/1000
p=eval(input("Enter Principal Amount:"))
r=eval(input("Enter Rate Amount:"))
t=eval(input("Enter the time period:"))
print("Simple Interest is:",SI(p,r,t))
