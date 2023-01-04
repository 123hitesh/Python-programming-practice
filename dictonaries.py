'''d1=()
print(d1)

d1={1:"abc",2:"def"}
print(d1)

d2={"EMP101":["Mohit Kumar",56000],"EMP102":["Rohit Kumar",65000]}
print(d2)

print(d1[1])
print(d2["EMP102"])
#print (d1[56])

print(d1.get(1))
print(d2.get("EMP101"))
print(d1.get(56))

for k,v in d2.items():
    print(k,'=',v)'''

'''list1=[10,20,30,40,50]
list2=["abc","xyz","rtf","hju"]
d1=dict(zip(list1,list2))
print(d1)

data1=input("data1: ")
list1=data1.split(',')

data2=input("data2: ")
list2=data2.split(',')
d2=dict(zip(list1,list2))
print(d2)'''

'''#program to creat a dictionary from 2 lists
data1=input("Data1: ")
data2=input("Data2: ")
l1=data1.split(',')
l2=data2.split(',')
d1={}
if (len(l1)==len(l2)):
    for i in range(len(l1)):
        d1[l1[i]]=l2[i]
    print(sorted(d1.items()))
else:
    print("length should be equal")'''

'''data1=input("Data1: ")
data2=input("Data2: ")
l1=data1.split(',')
l2=data2.split(',')
dict1=dict(zip(l1,l2))
key=input("key: ")
if key in dict1:
    print("value: ",dict1[key])
else:
    print("value: ",dict1.get(key,"None"))'''


           
