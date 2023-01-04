#greatest of 3 numbers with passing arguements
def great(a,b,c):
    if a>b and a>c:
        print("greatest is:",a)
    elif b>c:
        print("greatest is:",b)
    else:
        print("greatest is:",c)
great(1,2,3)
great(2,4,6)
great(28,49,64)
            
