percent=eval(input("enter the percentage:"))
if percent>90:
    print("The grade obtained from the", percent, "is A")
elif percent>80 and percent<=90:
    print("The grade obtained from the" ,percent, "is B")
elif percent>60 and percent<=80:
    print("The grade obtained from the" ,percent, "is C")
elif percent<60:
     print("The grade obtained from the" ,percent, "is D")
else:
    print("input valid percentage")
