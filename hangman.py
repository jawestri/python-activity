# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:33:30 2018

@author: jamiew
"""

import random

# display options below


def hangman_visual(num_wrong):
    if num_wrong == 0:
        print (" _______")
        print ("    |  |")
        print ("       |")
        print ("       |")
        print ("       |")
        print ("       |")
        print (" -------")

    elif num_wrong == 1:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("       |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif num_wrong == 2:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("    |  |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif num_wrong == 3:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|  |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif num_wrong == 4:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|/ |")
        print ("       |")
        print ("       |")
        print (" -------")
    elif num_wrong == 5:
        print (" _______")
        print ("    |  |")
        print ("    O  |")
        print ("   \|/ |")
        print ("   /   |")
        print ("       |")
        print (" -------")
    elif num_wrong == 6:
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
user_guess = []
word_list = ["phone", "quick", "water", "bravo", "table", "micro",
             "cable", "giant", "power", "laser", "video"]
word = random.choice(word_list)

blanks = "_" * 5
blanks_list = list(blanks)
print ("Guess the word: {:^5s}".format(' '.join(blanks_list)))
blanks_left = len(word)
count = 0
win = False
lose = False
num_wrong = 0
while win is not True and lose is not True:
    guess = input('Enter 1 letter:')
# if user guesses duplicate letter, display previous attempts
    if guess in user_guess:
        print("\nLetter already been guessed!\nYou've tried:%s" % user_guess)
    else:
        # check attempt letter againt each index in word
        # if correct, display loction of correct letter
        # if guess incorrect, inc. num of wrong guesses
            wrong = True
            for i in range(0, len(word)):
                if guess == word[i]:
                    blanks_list[i] = word[i]
                    print("correct guess!")
                    blanks_left -= 1
                    wrong = False
            if wrong is True:
                num_wrong += 1
                print("letter not in word")
# displaying hangman and progess of user
    count += 1
    hangman_visual(num_wrong)
    print ("{:^30s}".format(' '.join(blanks_list)))
    print("\n--------------------------------------------------------------\n")
    user_guess.append(guess)
# all blanks have been filled=user wins
    if blanks_left == 0:
        win = True
        print("Congrats, you won!!!!!")
    if num_wrong == 6:                        # user has beeen hanged
        print("Too many tries, you've been hanged")
        print("The word was %s" % word)
        lose = True

        