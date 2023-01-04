'''str1="This is my first String"
print(str1)
print(str1[11])
print(str1[-6])'''

'''str="How are you?"
print("String is",str)
print(str[4:7])
print(str[2:5])
print(str[-4:-1])
print(str[-2:-5:-1])
print(str[-4:])'''

'''a=input()
if len(a)<3:
    print(a)
else:
    print(a[0]+a[1]+a[-2:])'''


'''s=input("Enter the string: ")
print(s[1:-1])'''

s=input("Enter the string: ")
s1=s[0]
s2=s[-1]
if len(s)==0:
    print("null")
elif len(s)==1:
    print(s)
else:
    print(s2,s[1:-1],s1,sep='')
