# [Assignment 7] Vinayak Sahal vs9736

# import random
import random
from string import punctuation


# Part 1

# 1

# naming the make_matrix function
def make_matrix(nRows, nColumns):

    # making an empty matrix
    matrix = []

    # for loop to iterate over the rows
    for row in range(nRows):
        matrix.append([])

        # for loop for columns
        for column in range(nColumns):

            # appending random ints in range of (0,1)
            matrix[row].append(random.randint(0,1))

        # prints each new row on a seperate line
        print(matrix[row])

    # returning matrix
    return matrix


# 2

# naming the functions
def even_cols(matrix):

    # setting an empty list for column values
    columnList = []

    # for loop to go through each column of the matrix
    for column in range(len(matrix[0])):

        # setting count to 0 after each loop
        count = 0

        # for loop to go through each row
        for row in range(len(matrix)):

            # checking to too see if each value equals to 1
            if matrix[row][column] == 1:

                # adding to count if value equals to 1
                count += 1

        # printing the column if number of 1's is even
        if count % 2 == 0:
            columnList.append(column)

    # return the list containing all the column values
    return columnList


# Part 2

stop_words = {"a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"}

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def print_word_count(dictionary, word):
    print("Count of \"" + word + "\" is:", dictionary[word])

# 4

# naming the function
def count_words(file):

    # setting variables
     openFile = open(file, 'r')
     wordCounter = {}

     # for loop to go through each line
     for line in openFile:

         # for loop to go through each word
         for word in line.split():

             # strip the punctuation
             word = strip_punctuation(word)

             # make the words all lowercase
             word = word.lower()

             # checks to see if word is in stop words
             if word not in stop_words:

                 # checks to see if word has already been counted
                 if word in wordCounter:
                     num = wordCounter[word]
                     wordCounter[word] = num + 1
                 else:
                     wordCounter[word] = 1

     # returns wordCounter
     return wordCounter

# 5

# naming the function
def find_max(dictWords):

    # setting variables
    max = 0
    word = ''

    # for loop that goes through the dict
    for words in dictWords:

        # if statement to see if key is maximum
        if dictWords[words] > max:
            max = dictWords[words]
            word = words

    # returns tuple
    return (word, max)

# 6

# naming main function
def main():
    # part 1
    test = (make_matrix(6, 6))
    print(even_cols(test))

    # part 2
    counter = count_words('raven.txt')
    word, max = find_max(counter)
    print_word_count(counter, word)
    print_word_count(counter, 'raven')
    print_word_count(counter, 'nevermore')

# calling main
main()







