# assignment: Hangman(Programming Assignment 1)
# author: Mika Lim
# date: Sept 30 2022 - 
# file: hangman.py is a program that simulates a hangman word guessing game
# input: (write input description)
# output: (write output description)

import random

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

def generate_secret_word(wordSize):
    return random.choice(dictionary[wordSize])

def generate_public_word(wordSize):
    publicWord = []
    for i in range(wordSize):
        publicWord.append('__' )
    return publicWord

def update_public_word(currentWord, secretWord, newLetter):
    for i in range(len(secretWord)):
        if secretWord[i] == newLetter:
            currentWord[i] = newLetter.upper()
    print(*currentWord, sep=" ")



if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print("Welcome to the Hangman Game!")
    isPlaying = True
    gameRunning = False
    # START MAIN LOOP (OUTER PROGRAM LOOP)

    while isPlaying == True:
     

        ##WORD LENGTH SETUP
        print("Please choose a size of a word to be guessed [3 – 12, default any size]:")
        val  = input()
        if val == "" or val != range(3,12):
            wordSize = random.randint(3,12)
        else:
            wordSize = int(val)
        print('The word size is set to ', wordSize)
        secretWord = generate_secret_word(wordSize)
        publicWord = generate_public_word(wordSize)


        ## LIVES SETUP
        print('Please choose a number of lives [1 – 10, default 5]:')
        val2 = input()
        if val2 == ""or val != range(1,10):
            lives = 5
        else:
            lives = int(val2)
        print("You have ",lives," lives")
       

        ##GAME BEGINS
        print("Beginning Game...")
        lettersChosen = []
        gameRunning = True
        while gameRunning == True:
            
            print("Letters chosen:", *lettersChosen)
            print(*publicWord, sep=" ")
            print("lives:",lives)
            print("Please choose a new letter > ")

            inputLetter = input()
            if inputLetter in lettersChosen:
                print("You have already chosen this letter")
                continue
            print("secret word is",secretWord)

            ## CHECK LETTER IN WORD
            if inputLetter in secretWord:
                print(update_public_word(publicWord,secretWord,inputLetter))
                lettersChosen.append(inputLetter.upper())
            else:
                lives = lives - 1
                lettersChosen.append(inputLetter.upper())

            if lives == 0:
                print("You lost! The word is",secretWord.upper(),"!")
                gameRunning = False
            elif '__' not in publicWord:
                print("Congratulations!!! You won! The word is",secretWord.upper(),"!")
                gameRunning = False
        
        print("Would you like to play again [Y/N]?")
        answer = input()
        if answer.upper() == "Y":
            isPlaying = True
        elif answer.upper() == "N":
            print("Goodbye!")
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