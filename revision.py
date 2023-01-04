'''data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(',')
list2=data1.split(',')
dict1=dict(zip(list1,list2))
key=input("key: ")
if key in dict1:
    print("value: ",dict1.pop(key))
    sorted_dict=sorted(dict1.items())
    print("dictionary: ",sorted_dict)
else:
    print("key does not exists")'''

'''data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(',')
list2=data2.split(',')
dict1=dict(zip(list1,list2))
l1=[]
for key in dict1:
    l1.append(dict1[key])
l1.sort()
print("max: ",l1[-1])
print("min: ",l1[0])'''

'''data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(',')
list2=data2.split(',')
dict1=dict(zip(list1,list2))
key=input("key: ")
if key in dict1:
    val=input("value: ")
    dict1[key]=val
    print("sorted dictionary: ",sorted(dict1.items()))
else:
    print("key does not exists")'''

'''data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(',')
list2=data2.split(',')
d1=dict(zip(list1,list2))
print(all(d1))
print(any(d1))
print(len(d1))
sorted(d1)
print(sorted(d1))
print(sorted(d1.items()))'''

'''data1=input("data1: ")
data2=input("data2: ")
list1=data1.split(',')
list2=data2.split(',')
dict1=dict(zip(list1,list2))
d3=dict()
for key in dict1:
    d3[dict1[key]]=key
print("before exchange: ",sorted(dict1.items()))
print("after exchange: ",sorted(d3.items()))'''

data=input("Enter strings with # seperation")
list1=data.split("#")
for x in list1:
    print(x,len(x))






