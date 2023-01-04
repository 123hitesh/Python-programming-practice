price=eval(input("Enter the price of bike : "))
if price>100000:
    print("The tax added is 15% and road tax is",15/100*price)
elif price>50000 and price<=100000:
     print("The tax added is 10% and total road tax is",10/100*price)
else:
     print("The tax added is 5% and total road tax is",5/100*price)
    
