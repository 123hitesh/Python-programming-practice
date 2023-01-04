#function that return greatest of three numbers
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

print("Greatest Number is: ",greatest(23,24,25))
