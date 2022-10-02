# assignment: Hangman(Programming Assignment 1)
# author: Mika Lim
# date: Sept 30 2022 - 
# file: hangman.py is a program that simulates a hangman word guessing game
# input: (write input description)
# output: (write output description)

from random import choice, random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12  WHY?

def import_dictionary (filename) :
    dictionary = {}
    
    max_size = 12
   
    d = open('dictionary.txt', "r")
    for x in d:
       wordLength = len(x.strip())
       print(x.strip(),wordLength)
       if wordLength in dictionary:
        currentVal = dictionary[wordLength]
        currentVal.append(x.strip())
        dictionary[wordLength] = currentVal
       else:
            dictionary[wordLength] = [x.strip()]
    d.close()
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    pass 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    pass
    #return (size, lives)


# MAIN

def generate_word(wordSize):
    import random
    return random.choice(dictionary[wordSize])

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print("Welcome to the Hangman Game!")
    isPlaying = True

    # START MAIN LOOP (OUTER PROGRAM LOOP)

    while isPlaying == True:
        import random
        print("Please choose a size of a word to be guessed [3 – 12, default any size]:")
        if input() == "":
            wordSize = random.randint(3,12)
        else:
            wordSize = int(input())
        print('The word size is set to ', wordSize)
        secretWord = generate_word(wordSize)

        print('Please choose a number of lives [1 – 10, default 5]:')
        if input() == "":
            lives = 5
        else:
            lives = int(input())
        print("You have ",lives," lives")
        
        isPlaying = False


    

    # set up game options (the word size and number of lives)
    #lenChoice represents length of word

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    #wordList = dictionary[lenChoice]
    # word = choice(wordList )
    
        # START GAME LOOP   (INNER PROGRAM LOOP)

        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter

        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program