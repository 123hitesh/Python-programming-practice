
#write a program to copy the content of one file into another file

f=open('my.txt','r')
x=open('copy.txt','w')
str1=f.read()
x.write(str1)
x.close()
f.close()
