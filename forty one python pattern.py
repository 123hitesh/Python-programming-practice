def print_pattern(x):
    c=0
    for i in range(0,len(x)+1):
        print(x[0:c],end="")
        print()
        c=c+1
print_pattern("programming")
