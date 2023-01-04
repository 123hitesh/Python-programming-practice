#use of map function


'''def double(n):
    return n*2

l=[2,3,4,5,6,7,8,9]
l_updated = map(double,l)
print(list(l_updated)) '''


'''def sal_increase(n):
    return n+n*0.1
l_sal=[70000,67000,80000,90000,50000]
l_sal_update= map(sal_increase,l_sal)
print(list(l_sal_update))'''

'''radius=[2,3,4,5,6]
def area(r):
    return 3.14*r*r
cal_area=map(area,radius)
print(list(cal_area))'''

'''list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
def add(a,b):
    return a+b
added_list=map(add,list1,list2)
print(list(added_list))'''

'''list3=['abc','defgh','tghrd','yuivfdrrd']
len_list=map(lambda l : len(l),list3)
print(list(len_list))'''

'''radius=[7,8,9,10,11]
cal_area=map(lambda r : 3.14*r*r,radius)
print(list(cal_area))'''


#program to create 2 lists radius and height which contains 5 radius and 5 heights .Create a map function to print 5 volumes of cylinder

radius=[3,4,5,6,7]
height=[4,5,6,7,8]
def vol(r,h):
    return 3.14*r**2*h
cal_volume=map(vol,radius,height)
print(list(cal_volume))
