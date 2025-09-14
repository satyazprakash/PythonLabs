# This project is to create a project for guessing Game.
# This is our first No Guessing Game

import random

# Defining Variables

n = random.randint(1,100)
guess = int(input('Enter an integer from 1 to 100 :  '))

# Do a loop

while n  != 'guess':
    print
    if  guess < n :
        print (' Guess is low')
        guess = int(input('Enter and integer from 1 to 100: '))
    elif guess > n:
        print(' Guess is high')
        guess = int(input('Enter the integer from 1 to 100: '))
    else:
        print(' You guessed it : ' )
        break
    print
