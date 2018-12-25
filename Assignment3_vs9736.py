## [Assignment 3] Vinayak Sahal vs9736

#1

#import random to use the random functions
import random

 #randomly chooses a number between 0-2 to assign the value to the variable
# 0 = rock, 1 = paper, 2 = scissors
computerSelection = random.randint(0,3)

# user selects what move to play
userSelection = input('Choose rock, paper, or scissors:')

# user's move gets converted to all uppercase so its easier to read
userSelection = str(userSelection.upper())

# this section if when the computer selects rock
if (computerSelection == 0):
    if ((userSelection) == 'ROCK'):
        print('Computer is rock. You are rock.')
        print('Draw.')
    elif ((userSelection) == 'SCISSORS'):
        print('Computer is rock. You are scissors.')
        print('Computer wins.')
    elif ((userSelection) == 'PAPER'):
        print('Computer is rock. You are paper.')
        print('You win.')

# this section if when the computer selects paper
if (computerSelection == 1):
    if ((userSelection) == 'ROCK'):
        print('Computer is paper. You are rock.')
        print('Computer wins.')
    elif ((userSelection) == 'SCISSORS'):
        print('Computer is paper. You are scissors.')
        print('You win.')
    elif ((userSelection) == 'PAPER'):
        print('Computer is paper. You are paper.')
        print('Draw.')

# this section if when the computer selects scissors
if (computerSelection == 2):
    if ((userSelection) == 'ROCK'):
        print('Computer is scissors. You are rock.')
        print('You win.')
    elif ((userSelection) == 'SCISSORS'):
        print('Computer is scissors. You are scissors.')
        print('Draw.')
    elif ((userSelection) == 'PAPER'):
        print('Computer is scissors. You are paper.')
        print('Computer wins.') 


#2

import turtle

# user selects that shape to draw
userShape = input('Would you like to draw a circle, square, or triangle?')

# user selects what color the shape is
userColor = str(input('What color would you like?'))

user's shape gets converted to all uppercase so its easier to read
userShape = str(userShape.upper())

#  initializes the turtle object
v = turtle.Turtle()

# if user selects a circle
if (userShape == 'CIRCLE'):
    v.color(userColor)
    v.circle(20,360)

# if user selects a square
if (userShape == 'SQUARE'):
    v.color(userColor)
    v.forward(150)
    v.right(90)
    v.forward(150)
    v.right(90)
    v.forward(150)
    v.right(90)
    v.forward(150)

# if user selects a triangle
if (userShape == 'TRIANGLE'):
    v.color(userColor)
    v.circle(40,720,3)

# ends turtle and closes the window
turtle.bye()




