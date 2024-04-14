import random

top_of_range=input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Enter a number greater than 0 next time")
        quit()
else:
    print("Enter a valid number next time")
    quit()

random_number=random.randint(0,top_of_range)
guess=0

while True:
    guess_number=input("Make a guess: ")
    guess +=1
    if guess_number.isdigit():
        guess_number=int(guess_number)
    else:
        print("Enter a valid number")
        continue

    if guess_number == random_number:
        print("You guessed it correct!")
        break
    elif guess_number > random_number:
        print("Large guess , make a small guess")
    else:
        print("Small guess, make a larger guess")
    
print("You guessed in ", guess, "guessed")
