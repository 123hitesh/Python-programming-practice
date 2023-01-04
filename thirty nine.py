#create a function that will return True if number of vowels in string is even otherwise false
def vowels(x):
    count=0
    for t in x:
        if t in ['a','e','i','o','u']:
            count=count+1
    if count%2==0:
        return True
    else:
        return False

print(vowels("rohit kumar"))
