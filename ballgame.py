#game shuffles a list with blank spaces and a ball. takes input from user, matches index of ball with user guess and gives reply

import random as rnd

#initial list
my_list = [" ", "O", " ", " "]

#shuffle list
def shuffled_list(mylist):
    rnd.shuffle(mylist)
    return mylist

#take input from user for guess
def user_guess():
    guess = ""

    while guess not in [0,1,2,3]:
        guess = int(input("Enter your guess (0,1,2,3):  "))

        return guess
    
#match guess with actual index of ball
def check_guess(mylist, guess):
    if mylist[guess]== 'O':
        print ("YOU GOT IT RIGHT!")
        print(mylist)

    else:
        print("Better luck next time!")
        print(mylist)

mixed_list = shuffled_list(my_list)
guess = user_guess()

check_guess(mixed_list, guess)