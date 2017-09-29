#AI system
#
#Carlitos C-K


import random
import math


# config
low = 1
high = 100

# helper functions
def show_start_screen():
    print("*************************")
    print("* &Guess a Number A.I!& *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    guess = (current_low + current_high)//2
    return guess
    

def pick_number():
    
    print("Think of a number between " + str(low) + " and " + str(high) + " and I will try to guess it.")
    print()
    input("Please press ENTER to continue...")

    
def check_guess(guess):
    print("Is your number " + str(guess) + ".")

        
    while True:
        answer = input("Enter yes, lower, higher...")

        if answer == 'yes':
            return 0
        elif answer == 'lower':
            return 1
        elif answer == 'higher':
            return -1
        else:
            print("Type yes, lower, higher nothing else...")
    
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = guess
            
        elif check == 1:
            current_high = guess
              

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



