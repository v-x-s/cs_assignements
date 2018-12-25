#[Assignment 4] Vinayak Sahal vs9736

# 1

# assign 1458 to secret number
secretNumber = 1458

# sets number of guesses to 0
numGuesses = 0


# assign users guesses
print('I’m thinking of a number from 1 to 10000. Try to guess my '
      'number! (Enter 0 to stop playing.)')
userGuess = eval(input('Please enter your guess:'))

# while loop to see how many guesses it takes for user to guess the secret number
while (userGuess != secretNumber):

    # if statement to see if player wants to play
    if (userGuess == 0):
        print('Goodbye!')
        break

    if not (1 <= userGuess <= 10000):
        numGuesses += 1
        print('Your guess must be between 1 and 10000.')
        userGuess = eval(input('Please enter your guess:'))

    if (userGuess < secretNumber):
        numGuesses += 1
        print('Your guess is too low.')
        userGuess = eval(input('Please enter your guess:'))

    elif (userGuess > secretNumber):
        numGuesses += 1
        print('Your guess is too high.')
        userGuess = eval(input('Please enter your guess:'))

# if statement for when the userGuess doesn't meet the while loop criteria
if (userGuess == secretNumber):
    numGuesses += 1
    print('That\'s correct! You win!')
    print('You guessed my number in', numGuesses, 'guesses.')


# 2

# setting n for stars
n = 5

# for loop to run in range of n
for i in range(1, n + 1):

    # for loop for spaces
    for j in range(n - i):
        print(' ', end='')

    # for loop for stars
    for k in range(i):
        print('*', end='')

    # for loop to move to next line
    print('')

# 3

# import turtle
import turtle

# assign v to turtle
v = turtle.Turtle()

# distance to increment down the columns
ydistance = -40

# for loop for drawing rows
for x in range(10):

    # for loop for drawing columns
    for x in range(7):

        v.circle(20, 360)
        v.penup()
        v.forward(40)
        v.pendown()
    v.penup()
    v.goto(0, ydistance)
    v.pendown()
    ydistance -= 40

# ends the program
turtle.bye()
