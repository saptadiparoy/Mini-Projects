import random as rnd

num_to_guess = rnd.randint(0,100)

print (num_to_guess)

guesses = [0]

while True:
    user_guess = int(input("enter a number to guess between (0,100):    "))

    if user_guess > 100 :
        print("Please guess withing 0 to 100!")

    guesses.append(user_guess)

    if user_guess == num_to_guess:
            print (f"You got it!! the number was {num_to_guess}")
            print (f"number of guesses ---- >{(len(guesses)-1)}")
            break

    if guesses[-2]:
        if abs (num_to_guess - user_guess) < abs(guesses[-2]):
             print ("VERY WARM")

        else:
             print ("COLDER")
    
    else :
        if abs(num_to_guess - user_guess) <= 10:
              print ("warmm")

        else:
             print ("cold")

print (guesses)