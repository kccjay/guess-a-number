#AI system
#
#Carlitos C-K


import random
import math


# config
low = 1
high = 101

# helper functions
def show_start_screen():
    #guess number ai
    #:P You have entered my program 
    print("                                          ")
    print("   * :P YOU HAVE ENTERED MY PROGRAM *     ")
    print("                                          ")
    print("             @@@@@@@@@@@@                 ")
    print("             @          @                 ")
    print("             @          @ GUESS AI        ")
    print("   I AM      @          @@@@@@@@@@@@      ")
    print("  @@@@@@@@@@@@          @          @      ")
    print("  @          @          @          @      ")
    print("  @          @          @          @      ")
    print("##########################################")
    print("####    :     :  : :   :     :  :     ####")
    print("###    :   : WELCOME HUMAN!  :    :    ###")
    print("## :  :   :    :    :    :     :     :  ##")
    print("#                                        #")
    print("#                                        #")

def show_credits():
    print("##########################################")
    print("# :    :   :  :     :    :       :  ::  :#")
    print("#  :      :     :          :      :  :   #")
    print("#    :             :                     #")
    print("#   :   : GOODBYE MY HUMAN PAWN   :  :   #")
    print("#    :        :         :       :        #")
    print("##########################################")
        
    
def get_guess(current_low, current_high):
    guess = (current_low + current_high)//2
    return guess
    

def pick_number():
    print()
    print("******************************************")
    print("*RULES TO MY GAME:                       *")
    print("*Think before you press enter and your   *")
    print("*answers include yes, higher, lower.     *")
    print("******************************************")
    print()
    print("Think of a number between " + str(low) + " and " + str(high)+ " and I will try to guess it.")
    print()
    print()
    input("Please press ENTER to continue...")

    
def check_guess(guess):
    print()
    print("Is your number " + str(guess) + "??")
    print()

        
    while True:
        answer = input("Enter...")
        answer = answer.lower()
        
        if answer == 'yes' or answer == 'y' or answer == 'yeah':
            return 0
        elif answer == 'lower' or answer == 'l':
            return 1
        elif answer == 'higher' or answer == 'h':
            return -1
        else:
            print()
            print("!!!!!!!!!!!!!!!!!!")
            print("!Invaild response!")
            print("!!!!!!!!!!!!!!!!!!")
            print()

def show_result():
    print()
    print("***********************")
    print("* Yesss I got it!!!!! *")
    print("***********************")
    print()

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



