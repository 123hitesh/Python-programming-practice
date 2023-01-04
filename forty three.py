#program to check if there is a vowel at second character of string. if no print No Vowel
def abc(x):
    if x[1] in ['a','i','e','o','u']:
        return True
    else:
        return False
print(abc("Hello"))
print(abc("check"))
