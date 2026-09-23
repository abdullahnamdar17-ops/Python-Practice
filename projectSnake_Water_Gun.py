'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
youstr = int(input("Enter your Choice: 1 for snake, -1 for water, 0 for gun: "))
youDict = {"1 ": "snake", "-1" : "water", "0" : "gun"}
younum = youDict[youstr]

if computer == youstr:
    print("It's a Draw!")

elif computer == -1 and youstr == 0:
    print("You Won!")
elif computer == -1 and youstr == 1:
    print ("You Lose!")
elif computer == 0 and youstr == -1:
    print("You Lose!")
elif computer == 0 and youstr == 1:
    print("You Won!")
elif computer == 1 and youstr == -1:
    print("You Won!")
elif computer == 1 and youstr == 0:
    print("You Lose!")

else:
    print("Invalid Input!")