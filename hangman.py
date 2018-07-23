# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:33:30 2018

@author: jamiew
"""

import random

# hanged after 6 wrong letter guess attempts
#display options below
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
            
            
            
            
#setup
print("Welcome to Hangman!")
print("The words 5 letter and you get 6 wrong choices")
print("\n\n~~Starting Game~~\n")
user_guess = []
word_list=["phone","quick","water","bravo","table","micro","cable","giant","power"]
word = random.choice(word_list)

blanks = "_" * 5
blanks_list = list(blanks)
print ("Guess the word: {:^5s}".format(' '.join(blanks_list)))
blanks_left=len(word)
count = 0 
win = False
lose = False
num_wrong = 0



while win!= True and lose!=True:
    guess = input('Enter 1 letter:')

    if guess in user_guess:     #if user guesses duplicate letter, display previous attempts
        print("\nYou already guessed this letter!\nYou've tried:%s"  %user_guess)
    else:
            wrong= True
            for i in range(0,len(word)):    #check attempt letter againt each index in word
                if guess == word[i]:
                    blanks_list[i] = word[i]
                    print("correct guess!") #if correct, display loction of correct letter
                    blanks_left -=1 
                    wrong = False
            if wrong == True:               #if guess incorrect, inc. num of wrong guesses
                num_wrong +=1
                print("letter not in word")
                
            
    count +=1
    hangman_visual(num_wrong)  
    print ("{:^30s}".format(' '.join(blanks_list)))#displaying hangman and progess of user
    print("\n---------------------------------------------------------------\n")
    user_guess.append(guess)
    
    if blanks_left==0:                      #all blanks have been filled=user wins
        win=True
        print("Congrats, you won!!!!!")
        
    if num_wrong==6:                        #user has beeen hanged
        print("Too many tries, you've been hanged")
        print("The word was %s" %word)
        lose=True
        
        