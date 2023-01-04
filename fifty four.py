'''#working of docstring'''
'''def add(a,b):'''
'''  Author:abc
date of creation: 09-11-2022
This function will add two numbers'''
'''  return a+b
print(add.__doc__)
print("Sum is: ",add(12,34))'''


'''def var_arg(*v):
    for x in v:
        print(x)
var_arg(12,84)
var_arg('EMP101','ROHAN KUMAR','78000')
var_arg('red','green')
var_arg('1','ROHIT KUMAR','KOCO02')'''


def var_arg(**v):
    for x,y in v.items():
        print(x,'=',y)
var_arg(a=12,b=84)
var_arg(id='EMP101',name='ROHAN KUMAR',sal=78000)
var_arg(col1='red',col2='green')
var_arg(roll_no=1,name='ROHIT KUMAR',section='KOCO02')
