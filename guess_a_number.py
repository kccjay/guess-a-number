
import random
import math

# config
low = 1
high = 100
limit = math.log(high - low + 1, 2)
limit = math.ceil(limit)

# helper functions
def show_start_screen():
    print("")
    print("")
    print("")
    print("__                                       |>>      ")
    print("@@\                                      |>>>>  ")
    print("_!__                                     |>>    ")
    print("@@@@\                                    |      ")
    print("_!_!__                                   |      ")
    print("@@@@@ \                                  |            ")
    print("_!_!_!__   Guess my number!      ##      |      ##    ")
    print("@@@@@@@ \                       ####     |     ####   ")
    print("######################################################")
    print("####                                              ####")
    print("###                                                ###") 
    print("##                                                  ##")
    print("#                                                    #")

def show_credits():
    print("######################################################")
    print("#This awesome game was created by The Karlito Master.#")
    print("######################################################")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print()
            print("You must enter a number.")
            print()

def pick_number():
    print()
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You also have " + str(limit) + " atempts to guess my number")
    print()

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print()
        print("You guessed too low.")
        print()
    elif guess > rand:
        print()
        print("You guessed too high.")
        print()

def show_result(guess, rand):
    if guess == rand:
        print()
        print("You win!")
        print()
    else:
        print("You are such a loser! The number was " + str(rand) + ".")
        print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        #case-insensitive for decision
        decision = decision.lower()

        if decision == 'y' or decision == 'yes' or decision == 'yepper':
            return True
        elif decision == 'n' or decision == 'no' or decision == 'nope':
            return False
        else:
            print()
            print("Listen pumpkin spice, Please enter 'y' or 'n'!!!")
            print()

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
