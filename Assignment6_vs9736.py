# [Assignment 6] Vinayak Sahal vs9736

# 1

# naming the function
def locker_puzzle(lockers):

    # setting students to lockers
    students = lockers

    # making list of booleans
    opened = [False] * 101

    # for loop for students and lockers
    for s in range(1, students + 1):

        # for loop for opening/closing lockers
        for locker in range(s, lockers + 1, s):
            opened[locker] = not opened[locker]

    # for loop to check if locker is open and printing it
    for locker in range(1, lockers + 1):
        if opened[locker]:
            print(locker)

# making main function for locker_puzzle
def main():
    locker_puzzle(100)

# calling main
main()


# 2

# naming function
def get_guess():

    # setting secret word and dashes length
    secretWord = 'banjo'
    dashes = '-' * len(secretWord)

    # setting total number of guesses
    guessesLeft = 8

    # empty list of used letters
    usedLetters = []

    # prints welcome sequence
    print('Let\'s play hangman!')
    print(dashes)

    # while loop for conditions untill guesses = 0 and dashes not equal to word
    while (guessesLeft > 0) and not (dashes == secretWord):

        userGuess = input('Guess a letter: ')
        userGuess = userGuess.lower()

        # if statement to check if only a single letter is inputted
        if (userGuess.isalpha() == False) or (len(userGuess) != 1):
            print('This is not a letter. Enter a letter.')

        # else to check if proper letter is inputted
        else:

            # if statement to check if letter has been previously called
            if (userGuess in usedLetters):
                print('You\'ve already guessed ' + str(userGuess))

            # checks if user guess is in secretWord
            elif (userGuess in secretWord):
                dashes = updateDashes(secretWord, dashes, userGuess)
                usedLetters.append(userGuess)
                print(dashes)
                print('You have', (guessesLeft), 'tries remaining.')

            # checks if its a new letter and adds it to list
            elif (userGuess not in usedLetters):
                usedLetters.append(userGuess)
                guessesLeft -= 1
                print(dashes)
                print('You have', (guessesLeft), 'tries remaining.')

    # if guesses = 0 then game is over
    if guessesLeft == 0:
        print('You have 0 tries remaining.')
        print('You lose.')

    # if word guessed in the criteria then let user know they won
    else:
        print(secretWord)
        print('You win!')

# naming the function for updating dashes
def updateDashes(secretWord, dash, guess):

    # empty string to add dashes
    result = ''

    # if guessed letter in word then update the dashes accordingly
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            result += guess

        # if letter not in word dashes  manipulated accordingly
        else:
            result += dash[i]

    # returns result in the end
    return result

# naming main function
def main():
    get_guess()

# calling main
main()