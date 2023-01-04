'''str1=input('str1')
l1=str1.split()
print("List:",l1)

l2=[1,2,3,4,5,'abc','vgy']
print(l2)

l1=list(input("str1:").split())
print(l1)'''

'''data=input('data')
l1=data.split(,)
print("Data:" l1,sep=",")'''


'''l2=[1,2,3,4,5,['abc',7,8]]
print(l2[0])
print(l2[5])
print(l2[5] [0])'''

'''l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
l1[2]="abc"
print(l1)'''

'''l1=[1,2,3,4,5,6,7,8,9,10]
print(l1[1:3])
print(l1[::])
print(l1[::-1])
print(l1[-1:-9:-1])
print(l1[0:9:2])
for x in l1:
    print(x)'''

'''data=input("data: ")
list1=data.split(",")
print("list:",list1)
index=int(input("index: "))
if index<len(list1)and index>=-(len(list1)):
    print("element:",list1[index])
else:
    print("invalid")'''


'''#use of append and extend function
l1=[1,2,3,4,5]
print(l1)
l1.append('abc')
print(l1)
l1.append([5,6,7])
print(l1)
l1.extend([8,9,10])
print(l1)'''

'''data=input('data')
l1=data.split(',')
print("FIrst and last elements:",l1[0],l1[-1])'''

'''l1=list(eval(input("List: ")))
print(l1)
if l1[0]==3 or l1[-1]==3:
    print("True")
else:
    print("False")'''

'''a=list(input("Data1: ").split(","))
b=list(input("Data2: ").split(","))
n=eval(input())
print(a*n)
print(b*n)
print(a+b)'''

'''l1=list(input("List: "))
if l1[0]==l1[-1]:
    print("Equal")
else:
    print("Not Equal")'''

a=list(input("LIST 1: ").split(","))
print("Before Updation: ",a)
j=eval(input("Index: "))
if j<len(a) and j>=-len(a):
    value=input("Element: ")
    a[j]=value
    print("After Updation: ",a)
else:
    print("Invalid")



