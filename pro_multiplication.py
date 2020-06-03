import random
yn = input("Do you wanna build a mathman? y/n ")
if yn == "n":
    exit()

while yn == "y":
    x = int(random.choice(range(1, 100)))
    y = int(random.choice(range(1, 100)))
    s = 0
    xy = x * y
    problem = ("What is {} x {}? ".format(x, y))
    user_answer = int(input(problem))
    while user_answer != xy:
        print ("You are wrong, try again ")
        user_answer = int(input("Try again- "))
        s = s - 1
    yn = input("You are correct, would you like to go again? y/n ")
    s = s + 1
    t = str(s)
print ("Your score is " + t)
