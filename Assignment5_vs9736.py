# [Assignment 4] Vinayak Sahal vs9736

# 1

#  naming the function
def reverseStr(s):

    # making an empty string
    reversedString = ''

    # for loop runs through string and stitches it in reverse order
    for x in s:
        reversedString = x + reversedString

    # returns string
    return reversedString


# 2

# naming the function
def palindrome(s):

    # if statement to see if string is same reversed and normal
    if (reverseStr(s) == s):
        return True

    return False


# 3

# naming the function
def printPalindrome():

    # for loop so that it runs 3 times
    for x in range(3):

        # asks user for input
        word = str(input('Enter a word:'))

        # checks if user input is a palindrome
        if palindrome(word) == True:
            print('Palindrome!')
        else:
            print('Not a palindrome.')


# 4

# naming the function
def primeNum(num):

    # if statement to see if the number is prime and greater than 1
    if num > 1:

    # runs from 2 to the num in parameter
     for i in range(2,num):

         # if statement to check for divisors
        if (num % i == 0):
            return False
            # is this necessary? (break statement)
     else:
        return True

    else:
        return False


# 5

# naming the function
def emirp():

    # for loop to ask user input 3 times
    for x in range(3):
        s = str(input('Enter a number:'))

        # if statement to check if its a palindrome
        if palindrome(s) == True:
            print('Not an emirp.')

        # else statement checks other criteria
        else:
            reverseS = reverseStr(s)
            s = int(s)
            reverseS = int(reverseS)

            # for loop to see if user input (s) and reverse of (s) are both primes
            if primeNum(s) == True and primeNum(reverseS) == True:
                print('Emirp!')
            else:
                print('Not an emirp.')


# 6

# naming the function
def twinPrimes():

    # for loop to run till 1000
    for x in range(1001):

        # checks if x and x+2 are both primes
        if primeNum(x) == True and primeNum(x + 2) == True:
            print(str(x) + ',' + str(x + 2))


# main function
def main():
    printPalindrome()
    emirp()
    twinPrimes()


#calls main function
main()

