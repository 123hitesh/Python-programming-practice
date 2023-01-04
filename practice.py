#write a program to create a lists of strings and create another
#list which contain length of each element of list created
#finally create a dictionary which contains list 2 as keys and list 1 as values

str1=input('str1')
l1=str1.split()
print("List:",l1)

l2=[]
for i in range(len(l1)):
    l2.append(l1[i])
    
