#using a return statement in a function
def count_vowel(x):
    count=0
    for t in x:
        if t in ['a','e','i','o','u']:
            count=count+1
    return count
print("number of vowels are",count_vowel(" rohit kumar"))
