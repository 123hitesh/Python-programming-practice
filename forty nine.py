#write a function that will return true if a number is palindrome number

def pali(a):
    rev=0
    x=a
    while a!=0:
        t=a%10
        rev=rev*10+t
        a=a//10
    if x==rev:
        return True
    else:
        return False

a=int(input("enter a number: "))
print(pali(a))
