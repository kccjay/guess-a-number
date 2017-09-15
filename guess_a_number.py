import random

#config
low = 1
high = 100
limit = 10

#start game 
rand = random.randint(1,100)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#helper functions
def get_guess():
    while True:
        g = input("Take a guess: ")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number bro.")

#play the game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("Too low bro.")
    elif guess > rand:
        print("Too high bro.")

    tries +=1

#Tell player outcome
if guess == rand:
    print("Your a master guesser")
else:
    print("You lose. I was thinking of " + str(rand) + ".")
