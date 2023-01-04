#write a function to print the series 1,4,9,16,25

def series(a):
    for i in range(1,a+1):
        print(i*i)
       
a=eval(input("Enter the number: "))
series(a)
    
