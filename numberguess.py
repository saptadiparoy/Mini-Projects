#number guessing game
#initialise range
import random as rdm

picked_number = rdm.randint(0,99)
print(picked_number)

#welcome message and legend

print ("Hello! Welcome to the number guessing game! The rules are simple, the system has picked a number and you need to guess it.")
print ("when your guess is around 5 units or closer to the number - Very Warm \nwhen guess is 15 units or closer to number - warm" \
"\nwhen guess is 25 units or closer to number - cold \nwhen guess is 35 units or closer to number - Colder \nfarther than 35 units - way too cold.")


#creating an empty list that stores guesses
guesses = [0]

#running a loop for main game
while True:
    #takes guess input in integer form
    guess_num = int(input("Guess the number! (0-99):    "))

    #first check to ensure guess is within range
    if guess_num > 99 or guess_num < 0:
        print("Guess within Range!")

    #appending guess to earlier made list to store and count number of guesses
    guesses.append(guess_num)

    #conditions according to legend/rules, comparing number and checking
    if guess_num == picked_number:
        print (f"You won! The number was {picked_number}")
        print (f"It took you {len(guesses)-1} guesses")
        print (guesses)

    elif abs(guess_num - picked_number) <= 5:
        print ("Very Warm!")

    elif abs(guess_num - picked_number) <= 15:
        print ("warm!")

    elif abs(guess_num - picked_number) <= 25:
        print ("cold!")

    elif abs(guess_num - picked_number) <= 35:
        print ("colder!")

    else:
        print ("WAYY TOO COLD!!!")
