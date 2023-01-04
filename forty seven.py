#write a function to print the occurence of a particulat character in string
def str(a,b):
    count=0
    for x in a:
        if x==b:
            count=count+1
    return count
a=input("Enter the string: ")
b=input("Enter the character to search: ")
print(b,"found in",a,str(a,b),"times")
    
