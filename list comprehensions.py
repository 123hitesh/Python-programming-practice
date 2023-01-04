# list comprehension
'''list1=[x for x in range(1,11)]
print(list1)

list2=[x for x in "python"]
print(list2)

list3=[i for i in range(1,11) if i%2==0]
print(list3)

list4=[a*b for a in [1,2,3,4] for b in [1,2,3,4]]
print(list4)

list5=[a for a in [1,2,3,4] for b in [2,3,5,6] if a==b]
print(list5)'''

# dictionary comprehension
# d1={k:v for k,v in sequence

d1={i:i**2 for i in range(1,11)}
print(d1)

d2={i.lower(): i for i in "PYTHON"}
print(d2)

d3={i:chr(i) for i in range(65,85)}
print(d3)
