import random

sum = 0
while True:
    no = random.randint(1, 6)
    x = input("Enter y or n : ")
    if x =="n":
        break
    n = int(input("Enter number b/w 1 to 6 : "))
    if n > 6:
        break
    if no == 1:
        print("[-----]")
        print("[------]")
        print("[  o   ]")
        print("[------]")
        print("[------]")

    if no == 2:
        print("[------]")
        print("[  o   ]")
        print("[  o   ]")
        print("[------]")
        print("[------]")

    if no == 3:
        print("[-----]")
        print("[------]")
        print("[   o  ]")
        print("[ o   o]")
        print("[------]")
    if no == 4:
        print("[------]")
        print("[------]")
        print("[ o   o]")
        print("[ o   o]")
        print("[------]")
    if no == 5:
        print("[------]")
        print("[   o  ]")
        print("[ o   o]")
        print("[ o   o]")
        print("[------]")
    if no == 6:
        print("[-----]")
        print("[ o o o]")
        print("[ o o o]")
        print("[ o o o]")
        print("[------]")
    if no == n:
        print("winner ...")
    sum = sum + no

print("sum : ", sum)
