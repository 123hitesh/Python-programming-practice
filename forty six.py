add= lambda a,b: (a+b)
sub= lambda a,b: (a-b)
mul= lambda a,b: (a*b)
div= lambda a,b: (a/b)
while True:
    ch=input("Enter + for add, - for sub, *for mul, /for div and . for exit : ")
    if ch=="+":
        a=eval(input("Enter the first number: "))
        b=eval(input("Enter the second number: "))
        print("Sum is",add(a,b))

    elif ch=="-":
        a=eval(input("Enter the first number: "))
        b=eval(input("Enter the second number: "))
        print("Difference is",sub(a,b))

    elif ch=="*":
        a=eval(input("Enter the first number: "))
        b=eval(input("Enter the second number: "))
        print("Product is",mul(a,b))

    elif ch=="/":
        a=eval(input("Enter the first number: "))
        b=eval(input("Enter the second number: "))
        print("Quotient is",div(a,b))

    elif ch==".":
        break

    else:
        print("Invalid Input")
