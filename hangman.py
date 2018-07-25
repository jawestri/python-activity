# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:33:30 2018

@author: jamiew
"""

import random

# display options below


def hangman_visual(wrong):
    if wrong == 0:
        print (" _______")
        print ("    |  |")
        print ("       |")
        print ("       |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif wrong == 1:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("       |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif wrong == 2:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("    |  |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif wrong == 3:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|  |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif wrong == 4:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|/ |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif wrong == 5:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|/ |")
        print ("   /   |")
        print ("       |")
        print (" -------")
    elif wrong == 6:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|/ |")
        print ("   / \ |")
        print ("       |")
        print (" -------")

# setup
print("Welcome to Hangman!")
print("The word is 5 letters and you get 6 wrong choices")
print("\n\n~~Starting Game~~\n")
USERGUESS = []
WORDLIST = ["phone", "quick", "water", "bravo", "table", "micro",
            "cable", "giant", "power", "laser", "video"]
WORD = random.choice(WORDLIST)

BLANKS = "_" * 5
BLANKSLIST = list(BLANKS)
print ("Guess the word: {:^5s}".format(' '.join(BLANKSLIST)))
BLANKSLEFT = len(WORD)
COUNT = 0
WIN = False
LOSE = False
NUMWRONG = 0
while WIN is not True and LOSE is not True:
    GUESS = input('Enter 1 letter:')
# if user guesses duplicate letter, display previous attempts
    if GUESS in USERGUESS:
        print("\nLetter already been guessed!\nYou've tried:%s" % USERGUESS)
    else:
        # check attempt letter againt each index in word
        # if correct, display loction of correct letter
        # if guess incorrect, inc. num of wrong guesses
        WRONG = True
        for i in range(0, len(WORD)):
            if GUESS == WORD[i]:
                BLANKSLIST[i] = WORD[i]
                print("correct guess!")
                BLANKSLEFT -= 1
                WRONG = False
        if WRONG is True:
            NUMWRONG += 1
            print("letter not in word")

# displaying hangman and progess of user
    COUNT += 1
    hangman_visual(NUMWRONG)
    print ("{:^30s}".format(' '.join(BLANKSLIST)))
    print("\n--------------------------------------------------------------\n")
    USERGUESS.append(GUESS)

# all blanks have been filled=user wins
    if BLANKSLEFT == 0:
        WIN = True
        print("Congrats, you won!!!!!")
    if NUMWRONG == 6:                        # user has beeen hanged
        print("Too many tries, you've been hanged")
        print("The word was %s" % WORD)
        LOSE = True

       