import random

options = ["rock","paper","scissors"]
user_wins=0
computer_wins=0

while True:
    user_pick=input("Type rock, paper, scissors or Q to quit :").lower()
    computer_pick =options[random.randint(0,2)]

    if user_pick=="q":
        break

    if user_pick not in options:
        continue


    if user_pick=="rock" and computer_pick=="scissors":
        print("You Win")
        print("You picked :",user_pick,"computer picked :",computer_pick)
        user_wins+=1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("You win")
        print("You picked :",user_pick,"computer picked :",computer_pick)
        user_wins+=1
    elif user_pick=="paper" and computer_pick=="rock":
        print("You win")
        print("You picked :",user_pick,"computer picked :",computer_pick)
        user_wins+=1
    else:
        print("You Lost")
        print("You picked :",user_pick,"computer picked :",computer_pick)
        computer_wins+=1


print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")